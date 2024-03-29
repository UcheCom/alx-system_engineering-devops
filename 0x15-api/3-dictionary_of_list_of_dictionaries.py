#!/usr/bin/python3
"""This exports all employees data in JSON format"""

import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    reqt = requests.get(url)
    Users = reqt.json()

    dic_t = {}
    for u in Users:
        USER_ID = u.get('id')
        USERNAME = u.get('username')
        todos = '{}todos?userId={}'.format(url, USER_ID)
        req = requests.get(todos)
        tasks = req.json()

        dic_t[USER_ID] = []
        for t in tasks:
            TASK_COMPLETED_STATUS = t.get('completed')
            TASK_TITLE = t.get('title')
            dic_t[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(dic_t, jsonfile)
