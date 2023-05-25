#!/usr/bin/python3
"""
Script using REST API that returns info about a TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    """URL without path"""
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user_endpoint = "{}/users/{}".format(url, user_id)
    name = requests.get(user_endpoint).json().get("name")
    task_endpoint = "{}/todos".format(url)
    tasks = requests.get(task_endpoint).json()
    all_tasks = [dict for dict in tasks if dict.get("userId") == user_id]
    done_tasks = [dict for dict in all_tasks
                  if dict.get("completed") == True]

    print("Employee {} is done with tasks({}/{}):"
        .format(name, len(done_tasks), len(all_tasks)))
