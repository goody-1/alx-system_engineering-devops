#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Function to recurcively query a subreddit
    And return the hot topics for the subreddit

    Args:
        subreddit (str): The subreddit to query
        hot_list (list): Doesn't have to be passed
        after (str): Doesn't have to be passed
        # count (int): Doesn't have to be passed
    """

    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

        if after:
            url += f"&after={after}"

        response = requests.get(
            url,
            headers={"User-Agent": "web:alx_reddit:1.0 (by /u/atundeg)"},
            allow_redirects=False,
        )

        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]

            if not posts:
                return hot_list

            for post in posts:
                title = post["data"]["title"]
                hot_list.append(title)

            # Recursive call for next page
            new_after = data["data"]["after"]
            if new_after is not None:
                return recurse(subreddit, hot_list, new_after)
            return hot_list
        else:
            return None
    except Exception:
        return None
