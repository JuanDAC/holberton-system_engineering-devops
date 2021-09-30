#!/usr/bin/python3
"""
Module for storing the number_of_subscribers function.
"""
import requests

url = 'https://www.reddit.com/'


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers on a given subbreddit.
    """
    path = 'r/{}/about/.json'.format(subreddit)

    # get info of the subreddit
    response = requests.get("{}{}".format(url, path), allow_redirects=False)

    if response.status_code != 200:
        response.close()
        return 0

    data = response.json()
    response.close()

    subscribers = data.get('data').get('subscribers')

    # return the element data.subscribers
    return subscribers
