#!/usr/bin/python3
"""query reddit api"""

import requests


def number_of_subscribers(subreddit):
    """query reddit api and return no of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    header = {'User-Agent': 'My user Agent 1.0'}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        count_sub = data.get('subscribers', 0)
        return count_sub
    else:
        return 0
