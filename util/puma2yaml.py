#!/usr/bin/env python3

"""
Utility script to convert demo user input from csv to be used for initial user import
It is called puma, because of using the format of the list of users here:
https://gitlab.souvap-univention.de/souvap/tools/puma
"""

import csv
import sys

# 3rd party
import yaml


def create_user_object(user_name, first_name, last_name, password):
    """
    Create a user object adding conditional properties based on the user type
    """

    user_object = {
        "username": user_name,
        "firstname": first_name,
        "lastname": last_name,
        "primaryGroupCN": "Domain Users",
        "password": password,
    }

    if "admin" in user_name:
        user_object["primaryGroupCN"] = "Domain Admins"
    else:
        # TODO: there are other fields, that will need to be set,
        #       based on the admin status of a user, e.g. "isOxUser"
        pass

    return user_object


def main(input_file, password):
    """
    Iterate over a tab separated file containing one user per line
    with this order of fields: first name, last name, user name, e-mail address.
    Then create a yaml structure that can be used to import initial users to the
    SWP stack.
    NOTE: CSV header row is ignored
    """

    with open(input_file, "r", encoding="utf8") as users_file:
        users_reader = csv.reader(users_file, delimiter="\t")

        config_object = {
            "stackDataSwp": {
                "demoUsers": [],
            },
        }

        for row in users_reader:
            (first_name, last_name, user_name, email) = row
            config_object["stackDataSwp"]["demoUsers"].append(
                create_user_object(
                    user_name,
                    first_name,
                    last_name,
                    email,
                    password,
                ),
            )

        yaml.dump(data=config_object, sort_keys=False, stream=sys.stdout)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
