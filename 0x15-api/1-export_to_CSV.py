#!/usr/bin/python3
"""This exports the employee data in CSV format"""

import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    name = user.get('username')

    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    task1 = []
    for t in todos:
        task1.append([sys.argv[1], name,
                      t.get('completed'),
                      t.get('title')])

    filename = '{}.csv'.format(sys.argv[1])
    with open(filename, 'w') as csvfil:
        writer = csv.writer(csvfil, quoting=csv.QUOTE_ALL)

        for t in task1:
            writer.writerow(t)
