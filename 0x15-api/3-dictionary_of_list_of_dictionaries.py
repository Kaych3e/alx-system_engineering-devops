#!/usr/bin/python3
""" Python script to export data in the JSON format, record employee tasks """
import json
import requests
import sys

if __name__ == "__main__":
    """URL without path"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w", newline="") as jsonfile:
        json.dump({
            user.get("id"): [{
                    "task": tasks.get("title"),
                    "completed": tasks.get("completed"),
                    "username": user.get("username")
                    } for tasks in requests.get(
                        url + "todos",
                        params={"userId": user.get("id")}).json()]
            for user in users}, jsonfile)
