#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import json

import requests


def number_of_subscribers(subreddit):
    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        response = requests.get(
            url, headers={"User-Agent": "web:alx_reddit:1.0 (by /u/atundeg)"}
        )
        data = response.json()
        subscribers_count = data["data"]["subscribers"]

    except Exception:
        return 0
    return subscribers_count
