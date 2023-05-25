#!/usr/bin/python3
""" Python script to export data in the JSON format """
import json
import requests
import sys

if __name__ == "__main__":
    """URL without path"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_endPt = "users/{}".format(user_id)
    user = requests.get(url + user_endPt).json()
    username = user.get("username")
    tasks = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
                } for t in tasks]}, jsonfile)
