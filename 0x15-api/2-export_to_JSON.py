#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the JSON format.
"""


import json
from requests import get
from sys import argv


def getjson(d, p, q, v):
    return get('{}/{}?{}={}'.format(d, p, q, v)).json()


domine = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":
    user_id = argv[1]

    user = getjson(domine, 'users', 'id', user_id).pop()
    todo = getjson(domine, 'todos', 'userId', user_id)

    user_2_dict = {}
    user_2_dict[user_id] = []
    for task in todo:
        task_2_dict = {}
        task_2_dict['task'] = task.get('title')
        task_2_dict['completed'] = task.get('completed')
        task_2_dict['username'] = user.get('username')
        user_2_dict[user_id].append(task_2_dict)

    with open('{}.json'.format(user_id), "w") as file:
        json.dump(user_2_dict, file)
