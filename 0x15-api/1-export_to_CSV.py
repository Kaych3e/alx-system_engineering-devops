#!/usr/bin/python3
""" Python script to export data in the CSV format """
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_endPt = "users/{}".format(user_id)
    user = requests.get(url + user_endPt).json()
    username = user.get("username")
    tasks = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
            ) for t in tasks]
