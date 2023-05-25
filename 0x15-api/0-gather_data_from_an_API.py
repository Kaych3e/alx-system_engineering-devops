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
    name = requests.get(user_endpoint).json().get('name')
    task_endpoint = "{}/todos".format(url)
    tasks = requests.get(task_endpoint).json()
    all_tasks = [task for task in tasks if task.get("userId") == user_id]
    done_tasks = [task for task in all_tasks if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):"
            .format(name, len(done_tasks), len(all_tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
