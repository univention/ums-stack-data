#!/usr/bin/env python3

"""
Utility script to convert demo user input from csv to be used for initial user import
"""

import csv
import sys


def format(user_name, first_name, last_name, email):
    """
    Format the user data to match the Jinja2 Template format
    that is used in `process-join-data.py`
    """
    ldapBase = '{{ .ldapBase }}'
    return f'''---
action: "create"
module: "users/user"
position: "cn=users,{ldapBase}"
properties:
    username: "{user_name}"
    firstname: "{first_name}"
    lastname: "{last_name}"
    primaryGroup: "cn=Domain Admins,cn=groups,{ldapBase}"
    password: "SWPtester"
'''


def main(input_file):
    """
    Iterate over a tab separated file containing one user per line
    with this order of fields: first name, last name, user name, e-mail address.
    Then format the contents, so that they can be fed to `process-join-data.py`.
    NOTE: CSV header row is not handled
    """
    print("{{ with .Values.stackDataContext }}")

    with open(input_file, "r", encoding="utf8") as users_file:
        users_reader = csv.reader(users_file, delimiter="\t")

        for row in users_reader:
            (first_name, last_name, user_name, email) = row
            print(format(user_name, first_name, last_name, email))

    print("{{ end }}")


if __name__ == "__main__":
    main(sys.argv[1])
