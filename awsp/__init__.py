#!/usr/bin/python

import json
import sys

def remove_spaces(data):
    d = data.strip()
    return d.rstrip()


def print_env_vars(data):
    x = (
        '''
export AWS_ACCESS_KEY_ID={}
export AWS_SECRET_ACCESS_KEY={}
export AWS_SESSION_TOKEN="{}"
        '''.
            format(
                   data['Credentials']['AccessKeyId'],
                   data['Credentials']['SecretAccessKey'],
                   data['Credentials']['SessionToken'],
                   )
    )
    print(remove_spaces(x))


def run():
    data = remove_spaces(sys.stdin.read())
    try:
        j = json.loads(data)
        if 'Credentials' in j:
            print_env_vars(j)
        else:
            print("I couldn't find any credentials :(\nGot:")
            print(data)
    except ValueError as err:
        print("Couldn't fetch data, AccessDenied issue?")


if __name__ == "__main__":
    run()
