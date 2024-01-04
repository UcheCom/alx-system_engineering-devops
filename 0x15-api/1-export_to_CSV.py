#!/usr/bin/python3
"""This exports the employee data in CSV format"""

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    username = user.get('username')
    tasks = requests.get(url + "todos", params={"userId": user_id}).json()

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        for t in tasks:
            completed = t.get('completed')
            titletask = t.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id, username, completed, titletask))
