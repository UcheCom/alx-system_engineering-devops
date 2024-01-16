#!/usr/bin/python3
"""
This is module for count_words function
"""
from requests import get


def count_words(subreddit, word_list, after='',
                words_dict={}):
    """
    A recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords
    """

    word_list = map(lambda x: x.lower(), word_list)
    word_list = list(word_list)

    results = get("https://www.reddit.com/r/{}/hot.json"
                  .format(subreddit),
                  headers={'User-Agent': 'Uchecm1'},
                  params={'after': after},
                  allow_redirects=False)
    if results.status_code != 200:
        return

    try:
        resp = results.json().get('data', None)

        if resp is None:
            return
    except ValueError:
        return

    hot = resp.get('children', [])

    for post in hot:
        title = post.get('data', {}).get('title', '')
        for key_word in word_list:
            for word in title.lower().split():
                if key_word == word:
                    words_dict[key_word] = words_dict.get(key_word, 0) + 1

    after = resp.get('after', None)

    if after is None:
        sorted_dict = sorted(words_dict.items(),
                             key=lambda x: x[1],
                             reverse=True)

        for x in sorted_dict:
            if x[1] != 0:
                print("{}: {}".format(x[0], x[1]))
        return

    return count_words(subreddit, word_list,
                       after, words_dict)
