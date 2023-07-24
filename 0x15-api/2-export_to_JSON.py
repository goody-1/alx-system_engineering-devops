#!/usr/bin/python3
"""Export employee tasks to json"""

import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"{emp_url}/todos"

    total_tasks = requests.get(todos_url).json()
    done_tasks = requests.get(f"{todos_url}?completed=true").json()
    emp_uname = requests.get(emp_url).json().get("username")

    json_file = f"{emp_id}.json"

    for row in total_tasks:
        row["emp_id"] = emp_id
        row["username"] = emp_uname

    def transformed_data(data):
        transformed_data = {}
        d_list = []

        for item in data:
            row = {
                "task": item.get("title"),
                "completed": item.get("completed"),
                "username": item["username"],
            }
            d_list.append(row)
        transformed_data[emp_id] = d_list

        return transformed_data

    to_json = transformed_data(total_tasks)

    with open(json_file, "w") as file:
        json.dump(to_json, file, indent=2)
