#!/usr/bin/python3
""" Defines the function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed
"""
from requests import get
from sys import argv


def top_ten(subreddit):
    """ Prints the first 10 hot posts listed"""
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'limit': 10}
    user = {'User-agent': 'Uchecm1'}
    response = get(url, headers=user, params=params)
    resp = response.json()

    try:
        mydata = resp.get('data').get('children')
        for post in mydata:
            print(post.get('data').get('title'))

    except Exception:
        print("None")


if __name__ == "__main__":
    top_ten(argv[1])
