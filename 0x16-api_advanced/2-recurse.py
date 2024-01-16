#!/usr/bin/python3
""" Defines recursive function that queries the Reddit API and
    returns a list of hot articles
"""
from requests import get


def recurse(subreddit, hot_list=[], after="", count=0):
    """queries the all articles title"""
    global after
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'api_advanced-project'}
    params = {
        "after": after,
        "count": count,
        "limit": 50
    }
    response = get(url, headers=headers, params=params,
                   allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get('data')
    after = results.get('after')
    count += results.get('dist')
    for child in results.get('children'):
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
