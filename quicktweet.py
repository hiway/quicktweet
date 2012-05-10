#!/usr/bin/env python

import tweepy

try:
    from credentials import *
except:
    CONSUMER_KEY = ''
    CONSUMER_TOKEN = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''

def post_tweet(text):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_TOKEN)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(text)

if __name__ == '__main__':
    import sys
    import fileinput

    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
        post_tweet(text)
    else:
        tweeted = False
        for line in fileinput.input():
            tweeted = True
            post_tweet(line)

        if tweeted == False:
            print "Usage: %s [tweet]" % sys.argv[0]
