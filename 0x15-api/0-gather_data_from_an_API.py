#!/usr/bin/python3
"""This returns a to-do list information for a given employee ID."""
import requests
import sys

if __name__ == '__main__':
    id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    print("Employee {} is done with tasks".format(user.get('name')),
          end="")

    todos = requests.get(url + "todos", params={"userId": id}).json()
    task = []
    for t in todos:
        if t.get('completed'):
            task.append(t)

    print('({}/{}):'.format(len(task), len(todos)))
    for t in task:
        print('\t {}'.format(t.get('title')))
