#!/usr/bin/python3
"""This exports the employee data in JSON format"""

import sys
import json
import requests

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    name = user.get('username')

    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    filename = '{}.json'.format(user_id)
    with open(filename, 'w') as jsonfil:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": name
            } for t in todos]}, jsonfil)
