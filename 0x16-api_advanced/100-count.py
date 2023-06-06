#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and
prints a sorted count of given keywords.
"""
import requests
import sys


def count_words(subreddit, word_list, array=None, after=""):
    if array is None:
        array = {}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        result = response.json().get("data")
        after = result.get("after")

        for c in result.get("children"):
            split = c.get("data").get("title").lower().split()

            for word in word_list:
                if word.lower() in split:
                    number = len([n for n in split if n == word.lower()])
                    if array.get(word) is None:
                        array[word] = number
                    else:
                        array[word] += number

        if after:
            count_words(subreddit, word_list, array, after)
        else:
            result_count = sorted(array.items(), key=lambda x: (-x[1],
                                  x[0].lower()))
            for word, count in result_count:
                print("{}: {}".format(word.lower(), count))
