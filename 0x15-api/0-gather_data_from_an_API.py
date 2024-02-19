#!/usr/bin/python3
"""
Using an API to obtain data
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    """
    Returns information about his/her TODO list progress.
    """
    url_todos = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    url_name = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    response_todos = requests.get(url_todos)
    response_name = requests.get(url_name)
    todos = response_todos.json()
    name = (name := response_name.json()).get('name')
    tasks_num = len(todos)
    tasks_done = 0
    tasks = ""
    for i in range(tasks_num):
        if todos[i]['completed'] is True:
            tasks += f"\t {todos[i]['title']}\n"
            tasks_done += 1

    print(f"Employee {name} is done with \
tasks({tasks_done}/{tasks_num}):\n{tasks}", end="")
