# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2026 Univention GmbH

"""Resolve `kubernetes_secret` references in the template context."""

from typing import Protocol

REFERENCE_KEY = "kubernetes_secret"
REFERENCE_FIELDS = {"name", "key"}


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
