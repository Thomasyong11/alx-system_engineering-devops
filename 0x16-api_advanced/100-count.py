#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import re
import requests
import sys


def add_title(dictionary, hot_posts):
    """ Adds item into a list """
     if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        word_lower = word.lower()  # Convert the word to lowercase
        for key in dictionary.keys():
            if word_lower == key.lower():  # Use case-insensitive comparison
                dictionary[key] += 1
    add_title(dictionary, hot_posts[1:])  # Pass the rest of the list


def recurse(subreddit, dictionary, after=None):
    """ Queries to Reddit API """
     u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if after:
        recurse(subreddit, dictionary, after=after)

def count_words(subreddit, word_list):
    """ Init function """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    l = sorted(dictionary.items(), key=lambda kv: kv[1])
    l.reverse()

    if len(l) != 0:
        for item in l:
            if item[1] is not 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
