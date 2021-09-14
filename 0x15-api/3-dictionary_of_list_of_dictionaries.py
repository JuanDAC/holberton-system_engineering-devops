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
        id_user = user.get('id')
        users_2_dict[id_user] = []
        user_tacks = [
                {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.get("username")
                }
                for task in todos if id_user == task.get("userId")]
        users_2_dict[id_user] = user_tacks

    with open('todo_all_employees.json', "w", newline="") as file:
        json.dump(users_2_dict, file)
