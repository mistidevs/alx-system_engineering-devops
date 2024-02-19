#!/usr/bin/python3
"""
Using an API to obtain data
"""
import json
import requests
import sys


if __name__ == '__main__':
    """
    Returns information about his/her TODO list progress.
    Exports in JSON format.
    Returns all employees
    """
    url_all_users = f"https://jsonplaceholder.typicode.com/users/"
    response_all_users = requests.get(url_all_users)
    all_users = response_all_users.json()
    all_user_tasks = {}
    for user in all_users:
        user_name = user['name']
        id = user['id']
        url_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
        response_todos = requests.get(url_todos)
        todos = response_todos.json()
        all_user_tasks[f'{id}'] = []
        tasks_num = len(todos)
        for i in range(tasks_num):
            title = todos[i]['title']
            status = todos[i]['completed']
            all_user_tasks[f'{id}'].append({"username": f"{user_name}",
                                            "task": f"{title}",
                                            "completed": f"{status}"})

    with open("todo_all_employees.json", mode="w", encoding="utf-8") as f:
        json.dump(all_user_tasks, f)
