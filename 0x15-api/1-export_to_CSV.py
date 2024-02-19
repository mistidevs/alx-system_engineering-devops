#!/usr/bin/python3
"""
Using an API to obtain data
"""
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    """
    Returns information about his/her TODO list progress.
    Exports in CSV format.
    """
    user_id = argv[1]
    url_todos = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    url_name = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    response_todos = requests.get(url_todos)
    response_name = requests.get(url_name)
    todos = response_todos.json()
    name = (name := response_name.json()).get('name')

    with open(f"{user_id}.csv", mode="w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, name, t.get("completed"), t.get("title")]
        ) for t in todos]
