#!/usr/bin/python3
''' Fetches the progress of a TODO list from an employee given their id. '''
from requests import get
from sys import argv
getjson = lambda d, p, q, v: get('{}/{}?{}={}'.format(d, p, q, v)).json()
domine = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    user_id = argv[1]

    name = getjson(domine, 'users', 'id', user_id).pop()['name']
    todo = getjson(domine, 'todos', 'userId', user_id)

    task_complete = list()
    task_names = ""

    for task in todo:
        if task.get('completed') is True:
            task_complete.append(task)
            task_names += "\n\t{}".format(task.get('title'))

    formated = [name, len(task_complete), len(todo), task_names];
    text = 'Employee {} is done with tasks({}/{}):{}'.format(*formated);
    print(text)
