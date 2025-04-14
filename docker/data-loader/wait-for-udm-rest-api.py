#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023-2025 Univention GmbH


import logging
import os
import sys
import time

from univention.admin.rest.client import UDM

log = logging.getLogger("app")


class App:
    """
    Interim solution to wait for UDM Rest API's availability

    This script will loop until it can successfully talk to the UDM Rest API.
    The intended usage is to help with the need to model dependencies in
    container based deployments.
    """

    def __init__(self, udm):
        logging.basicConfig(level=logging.INFO)
        log.setLevel(logging.DEBUG)

        self.udm = udm
        self.timeout = int(os.environ.get("TIMEOUT", "600"))

    def run(self):
        start_time = time.time()
        while True:
            log.info("Checking if UDM Rest API can be reached...")
            try:
                self.udm.get_ldap_base()
                log.info("Success, UDM Rest API is available")
                break
            except Exception:
                pass

            if time.time() - start_time > self.timeout:
                log.error("Timeout reached, giving up")
                sys.exit(1)

            log.info("Unavailable, waiting 2 seconds")
            time.sleep(2)


def _connect_to_udm():
    udm_api_url = os.environ["UDM_API_URL"]
    log.info("Connecting to UDM API at URL %s", udm_api_url)
    udm_api_user = os.environ["UDM_API_USER"]
    with open(os.environ["UDM_API_PASSWORD_FILE"], "r") as password_file:
        udm_api_password = password_file.read()
    udm = UDM.http(udm_api_url, udm_api_user, udm_api_password)
    return udm


if __name__ == "__main__":
    udm = _connect_to_udm()
    app = App(udm)
    app.run()
