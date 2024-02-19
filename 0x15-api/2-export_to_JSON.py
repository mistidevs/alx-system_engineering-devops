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
    Exports in JSON format.
    """
    user_id = argv[1]
    url_todos = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    url_name = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    response_todos = requests.get(url_todos)
    response_name = requests.get(url_name)
    todos = response_todos.json()
    name = (name := response_name.json()).get('name')
    tasks_num = len(todos)

    all_tasks = {f"{user_id}": []}
    for i in range(tasks_num):
        title = todos[i]['title']
        status = todos[i]['completed']
        all_tasks[f"{user_id}"].append({"task": f"{title}",
                                        "completed": f"{status}",
                                        "username": f"{name}"})

    with open(f"{user_id}.json", mode="w", encoding="utf-8") as f:
        json.dump(all_tasks, f)
