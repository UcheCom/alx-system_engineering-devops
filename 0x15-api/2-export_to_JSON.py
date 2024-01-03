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

    todos = requests.get(url + "todos", params={"userId": USER_ID}).json()
    dic_t = {USER_ID: []}
    for t in todos:
        TASK_COMPLETED_STATUS = t.get('completed')
        TASK_TITLE = t.get('title')
        dic_t[USER_ID].append({
                              "task": TASK_TITLE,
                              "completed": TASK_COMPLETED_STATUS,
                              "username": USERNAME})
    filename = '{}.json'.format(USER_ID)
    with open(filename, 'w') as jsonfil:
        json.dump(dic_t, jsonfil)
