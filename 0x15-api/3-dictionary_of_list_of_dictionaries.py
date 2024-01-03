#!/usr/bin/python3
"""This exports all employees data in JSON format"""

import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + 'users').json()

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump({
            u.get('id'): [{
                'task': t.get('title'),
                'completed': t.get('completed'),
                'username': u.get('username')
            } for t in requests.get(url + 'todos',
                                    params={'userId': u.get('id')}).json()]
            for u in users}, jsonfile)
