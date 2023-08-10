#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(
        url, headers={"User-Agent": "web:alx_reddit:1.0 (by /u/atundeg)"}
    )

    data = response.json()

    subscribers_count = data["data"]["subscribers"]
    print(f"Subscribers count of /r/{subreddit}: {subscribers_count}")
    return subscribers_count
