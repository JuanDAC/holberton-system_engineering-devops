#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the JSON format.
"""


import json
from requests import get


def getjson(d, p):
    return get('{}/{}'.format(d, p)).json()


domine = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":

    users = getjson(domine, 'users')
    todos = getjson(domine, 'todos')

    users_2_dict = {}
    i = 0
    for user in users:
        users_2_dict[user.get('id')] = []
        while(i < len(todos)):
            if todos[i].get('userId') == user.get('id'):
                task_2_dict = {}
                task_2_dict['username'] = user.get('username')
                task_2_dict['task'] = todos[i].get('title')
                task_2_dict['completed'] = todos[i].get('completed')
                users_2_dict[user.get('id')].append(users_2_dict)
                i += 1

    with open('todo_all_employees.json', "w") as file:
        json.dump(users_2_dict, file)
