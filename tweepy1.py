#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:20:02 2019

@author: ashutosh
"""

import tweepy
from textblob import TextBlob
#keys required for generation of an API object
consumer_key = '5nv3plDx7he3ChuzX24FaujlD'
consumer_key_secret = 'UylYJSmusCT8DDN8q1KqbYbDDLc8BzPrDB9VrMUVeow05tryVO' 
access_token = '3343301473-MLyQRgCGU3HGaAhudUJ8c8DwXOeJezkMzOW7Agg'
access_token_secret = 'WTtayPHmNc1OoF4SavB7ZV5aFXKQO9sMyhTiF2K45yLgj' 
#authenticating using the keys generated
authenticate = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
authenticate.set_access_token(access_token,access_token_secret)
api = tweepy.API(authenticate)
#search for a tweets by a particular person or related to particular topic
tweets = api.search('Bill Gates')
for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    #following two lines display how textblob easily tokenizes text and even helps you in Parts of Speech Tagging
    #print(analysis.words)
    #print(analysis.tags)
    print(analysis.sentiment)
    #analysis.sentiment[0] contains polarity whereas analysis.sentiment[1] contains subjectivity which denotes how much of personal opinion is there in tweet
    if analysis.sentiment[0]>0:
        print('Positive')
    elif analysis.sentiment[0]<0:
        print('Negative')
    else:
        print('Neutral')
    print('\n')
