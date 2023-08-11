#!/usr/bin/python3
"""
Parses the title of all hot articles,\
 and prints a sorted count of given keywords
"""
from collections import Counter

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Function to recurcively query a subreddit\
 and prints a sorted count of given keywords

    Args:
        subreddit (str): The subreddit to query
        word_list (list): Doesn't have to be passed
        after (str): Doesn't have to be passed
        count (int): Doesn't have to be passed
    """

    if counts is None:
        counts = Counter()
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
                return

            for post in posts:
                title = post["data"]["title"]
                for word in word_list:
                    title_with_spaces = f" {title.lower()} "
                    word_with_spaces = f" {word.lower()} "
                    if word_with_spaces in title_with_spaces:
                        # Count the occurrences of the keyword within the title
                        occurrences = title_with_spaces.count(word_with_spaces)
                        counts[word] += occurrences

            # Recursive call for next page
            new_after = data["data"]["after"]
            if new_after is None:
                sorted_counts = sorted(
                    counts.items(), key=lambda x: (-x[1], x[0])
                )
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
                return
            return count_words(subreddit, word_list, new_after, counts)
        else:
            return None
    except Exception:
        return None
