#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023-2025 Univention GmbHimport dns.resolver

import logging
import os
import sys
from urllib.parse import urlparse

import dns.resolver
import requests

log = logging.getLogger("app")


class App:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        log.setLevel(logging.DEBUG)
        self.udm_api_user = os.environ["UDM_API_USER"]
        self.udm_api_password_file = os.environ["UDM_API_PASSWORD_FILE"]
        self.udm_api_url = urlparse(os.environ["UDM_API_URL"])
        self.udm_api_port = os.environ["UDM_API_PORT"]

    def _get_udm_password(self):
        with open(self.udm_api_password_file, "r") as passwd_file:
            password = passwd_file.read().strip()
        return password

    def discover_pods_ips(self):
        udm_api_ips = dns.resolver.resolve(self.udm_api_url.hostname, "A", search=True)
        return [ip.address for ip in udm_api_ips]

    def reload_pod_cache(self, ip):
        log.info("Refreshing cache for %s", ip)
        headers = {"Accept": "application/json"}
        response = requests.get(
            f"http://{ip}:{self.udm_api_port}/udm/users/user/add",
            auth=(self.udm_api_user, self._get_udm_password()),
            headers=headers,
        )
        if response.status_code == 200:
            log.info("Cache refreshed")
        else:
            log.error("Failed to refresh cache: %s", response.text)

    def run(self):
        pods_ips = self.discover_pods_ips()
        for pod_ip in pods_ips:
            self.reload_pod_cache(pod_ip)


def run():
    if not os.environ.get("UDM_API_USER"):
        log.info("Not refreshing udm-rest-api caches because UDM_API_USER is not set")
        sys.exit()
    app = App()
    app.run()


if __name__ == "__main__":
    run()
