# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2026 Univention GmbH

"""Resolve `kubernetesSecret` references in the template context."""

import base64
import os
from pathlib import Path
from typing import Protocol

import requests

REFERENCE_KEY = "kubernetesSecret"
REFERENCE_FIELDS = {"name", "key"}
SERVICE_ACCOUNT_DIR = Path("/var/run/secrets/kubernetes.io/serviceaccount")


class InvalidReference(ValueError):
    pass


class SecretReadError(RuntimeError):
    """A referenced Secret or key could not be read. The message never contains the value."""


class SecretReader(Protocol):
    def get(self, name: str, key: str) -> str: ...


def is_reference(node) -> bool:
    return isinstance(node, dict) and REFERENCE_KEY in node


def resolve_references(node, reader: SecretReader, path: str = ""):
    if is_reference(node):
        name, key = _validate(node, path)
        try:
            return reader.get(name, key)
        except SecretReadError as error:
            raise SecretReadError(f"{path or '<root>'}: {error}") from error
    if isinstance(node, dict):
        return {key: resolve_references(value, reader, _join(path, key)) for key, value in node.items()}
    if isinstance(node, list):
        return [resolve_references(item, reader, f"{path}[{index}]") for index, item in enumerate(node)]
    return node


def _validate(node: dict, path: str) -> tuple[str, str]:
    spec = node[REFERENCE_KEY]
    if (
        len(node) != 1
        or not isinstance(spec, dict)
        or set(spec) != REFERENCE_FIELDS
        or not all(isinstance(spec[field], str) and spec[field] for field in REFERENCE_FIELDS)
    ):
        raise InvalidReference(
            f"Invalid reference at {path or '<root>'}: "
            f"expected {{{REFERENCE_KEY}: {{name: <non-empty string>, key: <non-empty string>}}}}",
        )
    return spec["name"], spec["key"]


def _join(path: str, key) -> str:
    return f"{path}.{key}" if path else str(key)


class KubernetesSecretReader:
    """Reads Secrets from the pod's own namespace with its ServiceAccount token."""

    def __init__(self, service_account_dir: Path = SERVICE_ACCOUNT_DIR, session: requests.Session | None = None):
        self.service_account_dir = Path(service_account_dir)
        self.session = session
        self._secrets: dict[str, dict[str, str]] = {}

    def get(self, name: str, key: str) -> str:
        if name not in self._secrets:
            self._secrets[name] = self._fetch(name)
        data = self._secrets[name]
        if key not in data:
            raise SecretReadError(f"Secret {name} has no key {key}")
        try:
            return base64.b64decode(data[key]).decode("utf-8")
        except UnicodeDecodeError:
            raise SecretReadError(f"Secret {name} key {key} is not UTF-8") from None

    def _fetch(self, name: str) -> dict[str, str]:
        directory = self.service_account_dir
        namespace = (directory / "namespace").read_text().strip()
        token = (directory / "token").read_text().strip()
        api = f"https://{os.environ['KUBERNETES_SERVICE_HOST']}:{os.environ['KUBERNETES_SERVICE_PORT']}"
        session = self.session or requests.Session()
        response = session.get(
            f"{api}/api/v1/namespaces/{namespace}/secrets/{name}",
            headers={"Authorization": f"Bearer {token}"},
            verify=str(directory / "ca.crt"),
            timeout=10,
        )
        if response.status_code == 404:
            raise SecretReadError(f"Secret {name} not found in namespace {namespace}")
        if response.status_code == 403:
            raise SecretReadError(f"Access to Secret {name} in namespace {namespace} denied")
        if response.status_code != 200:
            raise SecretReadError(
                f"Reading Secret {name} in namespace {namespace} failed with HTTP {response.status_code}",
            )
        return response.json().get("data") or {}
