#!/usr/bin/env python3

"""
Utility script to convert demo user input from csv to be used for initial user import
"""

import csv
import sys


def format(user_name, first_name, last_name, email, password):
    """
    Format the user data to match the Jinja2 Template format
    that is used in `process-join-data.py`
    """

    ldapBase = '{{ .ldapBase }}'

    primaryGroupCN = "Domain Users"
    isOxUser = "Not"
    nonAdminFeatures = [
        'swpFileshareEnabled: "TRUE"',
        'swpProjectmanagementEnabled: "TRUE"',
        'swpKnowledgemanagementEnabled: "TRUE"',
        'swpLivecollaborationEnabled: "TRUE"',
    ]

    nonAdminFeaturesFormatted = "\n".join([f"    {feature}" for feature in nonAdminFeatures])

    if "admin" in user_name:
        primaryGroupCN = "Domain Admins"
        isOxUser = "OK"
        nonAdminFeaturesFormatted = ""

    return f'''---
action: "create"
module: "users/user"
position: "cn=users,{ldapBase}"
properties:
    username: "{user_name}"
    firstname: "{first_name}"
    lastname: "{last_name}"
    primaryGroup: "cn={primaryGroupCN},cn=groups,{ldapBase}"
    PasswordRecoveryEmail: "{email}" 
    password: "{password}"
    isOxUser: "{isOxUser}"
{nonAdminFeaturesFormatted}
'''


def main(input_file, password):
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
            print(format(user_name, first_name, last_name, email, password))

    print("{{ end }}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
