#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        response = requests.get(
            url, headers={"User-Agent": "web:alx_reddit:1.0 (by /u/atundeg)"}
        )
        if response.status_code == 200 and not response.is_redirect:
            data = response.json()
            posts = data["data"]["children"]

            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)
    except Exception:
        print(None)
