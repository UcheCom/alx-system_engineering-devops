#!/usr/bin/python3
"""This exports the employee data in JSON format"""

import json
import requests
import sys

if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + 'users/{}'.format(USER_ID)).json()
    USERNAME = user.get('username')

    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    filename = '{}.json'.format(USER_ID)
    with open(filename, 'w') as jsonfil:
        json.dump({USER_ID: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": USERNAME
            } for t in todos]}, jsonfil)
