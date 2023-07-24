#!/usr/bin/python3
"""Export all employees' tasks to json"""

import json
import requests


if __name__ == "__main__":
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    emp_url = "https://jsonplaceholder.typicode.com/users"

    all_tasks = requests.get(todos_url).json()

    json_file = "todo_all_employees.json"

    for task in all_tasks:
        emp = requests.get(f"{emp_url}/{task.get('userId')}").json()
        emp_uname = emp.get("username")
        task["username"] = emp_uname

    def transformed_data(data):
        transformed_data = {}

        for item in data:
            emp_id = item.get("userId")
            row = {
                "username": item.get("username"),
                "task": item.get("title"),
                "completed": item.get("completed"),
            }
            if emp_id not in transformed_data:
                d_list = []
                d_list.append(row)
                transformed_data[emp_id] = d_list
            else:
                transformed_data[emp_id].append(row)

        return transformed_data

    to_json = transformed_data(all_tasks)

    with open(json_file, "w") as file:
        json.dump(to_json, file, indent=2)
