#!/usr/bin/python3
"""
Module for storing the recurse function.
"""
import requests

get requests.get
url = 'https://www.reddit.com/'
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Custom User Agent 1.0.1',
    "Content-Type": "application/json",
})
query = {'limit': 100, 'after': after, }


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list with all of the hot articles on a given subbreddit.
    """
    path = 'r/{}/hot/.json'.format(subreddit)
    url = "{}{}".format(url, path)

    # get info of the subreddit
    response = get(url, allow_redirects=False, params=query, headers=headers)

    if response.status_code == 200:
        data = response.json()
        data = data.get('data')
        for item in data.get('children'):
            hot_list.append(item.get('data').get('title'))

    if response.status_code != 200:
        return None

    response.close()

    if data.get('after') is None:
        return hot_list

    return recurse(subreddit, hot_list, data.get('after'))
