#!/usr/bin/python3
""" Defines the function that queries the Reddit API and returns
   the number of subscribers.
"""
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """ This returns the number subscribers,
       returns 0 if the request is invalid
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user = {'User-agent': 'Uchecm1'}
    response = get(url, headers=user)
    resp = response.json()

    try:
        return resp.get('data').get('subscribers')
    except Exception:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1])
