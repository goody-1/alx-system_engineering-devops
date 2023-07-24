#!/usr/bin/python3
"""Export employee tasks to csv"""

import csv
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"{emp_url}/todos"

    total_tasks = requests.get(todos_url).json()
    done_tasks = requests.get(f"{todos_url}?completed=true").json()
    emp_uname = requests.get(emp_url).json().get("username")

    csv_file = f"{emp_id}.csv"
    fields_to_include = [
        "emp_id",
        "username",
        "completed",
        "title",
    ]

    for row in total_tasks:
        row["emp_id"] = emp_id
        row["username"] = emp_uname

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields_to_include)
        # writer.writeheader()

        for row in total_tasks:
            writer.writerow({field: row[field] for field in fields_to_include})
