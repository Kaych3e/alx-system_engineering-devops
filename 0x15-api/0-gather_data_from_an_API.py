#!/usr/bin/python3
"""
Script using REST API that returns info about a TODO list progress
""" 
import requests
import sys

if __name__ == "__main__":
    """URL without path"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = int(sys.argv[1])
    user_endpoint = "{}/users/{}".format(url, user_id)
    name = requests.get(user_endpoint).json()
    task_endpoint = "{}/todos".format(url, user_id)
    tasks = requests.get(task_endpoint).json()
    all_tasks = [task for task in tasks if task.get("completed") is True]
    done_tasks = [task.get("task") for task in tasks 
                  if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):"
            .format(name.get("name"), len(all_tasks), len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task))
