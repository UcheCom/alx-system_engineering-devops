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

    filename = "'{}.csv'.format(user_id)"
    with open(filename, 'w', newline="") as csvfil:
        writer = csv.writer(csvfil, quoting=csv.QUOTE_ALL)
        [writer.writerow(
             [user_id, username, t.get("completed"), t.get("title")]
         ) for t in tasks]
