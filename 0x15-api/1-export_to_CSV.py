#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the CSV format.
"""

import csv
import json
from requests import get
from sys import argv


def getjson(d, p, q, v):
    return get('{}/{}?{}={}'.format(d, p, q, v)).json()


domine = 'https://jsonplaceholder.typicode.com'
keys = {'delimiter': ',', 'quotechar': '"', 'quoting': csv.QUOTE_ALL}


if __name__ == "__main__":
    user_id = argv[1]

    user = getjson(domine, 'users', 'id', user_id).pop()
    todo = getjson(domine, 'todos', 'userId', user_id)

    with open('{}.csv'.format(user_id), mode='w') as file:
        for task in todo:
            writer = csv.writer(file, **keys)
            data = [user_id, user.get('username'),
                    task.get('completed'), task.get('title')]
            writer.writerow(data)
