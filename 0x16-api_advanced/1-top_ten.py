#!/usr/bin/python3
""" 
Module for storing the top_ten function.
"""

import requests 

get = requests.get
headers = requests.utils.default_headers()
headers.update({'User-Agent': 'My User Agent 1.0', })
query = {'limit': 10}


def top_ten(subreddit):
    """
    Prints titles of the first 10 hot posts listed in subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=headers, params=query, allow_redirects=False)
    if response.status_code is not 200:
        return print('None')

    r = response.json()
    data = r.get('data')
    children = data['children']
    for item in children:
        print(item.get('data')['title'])
