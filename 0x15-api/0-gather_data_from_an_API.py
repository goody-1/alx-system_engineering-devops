#!/usr/bin/python3
"""Return Employee task information from REST API"""
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"{emp_url}/todos"

    total_tasks = requests.get(todos_url).json()
    done_tasks = requests.get(f"{todos_url}?completed=true").json()
    emp_name = requests.get(emp_url).json().get("name")

    text = f"Employee {emp_name} is done with tasks\
({len(done_tasks)}/{len(total_tasks)}):"

    print(text)
    for task in done_tasks:
        print(f"\t {task.get('title')}")
