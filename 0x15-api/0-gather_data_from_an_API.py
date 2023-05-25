#!/usr/bin/python3
"""
Script using REST API that returns info about a TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    """URL without path"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_endPt = "users/{}".format(user_id)
    user = requests.get(url + user_endPt).json()
    tasks = requests.get(url + "todos", params={"userId": user_id}).json()

    comp_tasks = [t.get("title") for t in tasks if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
        .format(user.get("name"), len(comp_tasks), len(tasks)))
    [print("\t {}".format(c)) for c in comp_tasks]
