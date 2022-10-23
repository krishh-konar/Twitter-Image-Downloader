#!/usr/bin/python

''' 
A script that downloads all the pictures posted by a given twitter handle.

Author: Krishanu Konar
email: krishanukonar@gmail.com
'''

import API_Tokens as tokens
from tweepy import OAuth2BearerHandler, API
import os
import wget
import sys

MEDIA_FORMATS = {
    # https://help.twitter.com/en/using-twitter/tweeting-gifs-and-pictures
    "images": [ "jpg", "jpeg", "png", "webp", "heic" ],
    "videos": [ "mp4", "m4v", "mov" ],
    "gifs": [ "gif" ]
}

def main():
    #Authentication
    api = authenticate()

    print ('\nTwitter Image Downloader:\n========================\n')
    
    username = input("\nEnter the twitter handle of the Account to download media from: ")
    max_tweets = int(input("Enter Max. number of tweets to search (default: 1000): ") or 1000)
    media_formats = input("Enter type of media (images/gifs/videos/all) (default: images) ") or "images"
    
    all_tweets = getTweetsFromUser(api, username, max_tweets)
    media_URLs = getTweetMediaURL(all_tweets, media_formats)
    
    downloadFiles(media_URLs,username)
    print('\n\nFinished Downloading.\n')

def getTweetsFromUser(api, username, max_tweets=1000):
    '''
        Fetches Tweets from user with the handle 'username' 
        upto max of 'max_tweets' tweets.
    '''

    last_tweet_id = 0

    try:
        raw_tweets = api.user_timeline(screen_name=username, include_rts=False, exclude_replies=True)
    except Exception as e:
        print (e)
        sys.exit(-1)

    last_tweet_id = int(raw_tweets[-1].id - 1)
    
    print ('\nFetching tweets.....')

    while len(raw_tweets) < max_tweets:
        sys.stdout.write("\rTweets fetched: %d" % len(raw_tweets))
        sys.stdout.flush()

        tweets = api.user_timeline(screen_name=username, max_id=last_tweet_id, \
                    include_rts=False, exclude_replies=True)

        if len(tweets) == 0:
            break

        else:
            last_tweet_id = int(tweets[-1].id - 1)
            raw_tweets = raw_tweets + tweets

    print ('\nFinished fetching ' + str(min(len(raw_tweets),max_tweets)) + ' Tweets.')
    return raw_tweets

def getTweetMediaURL(all_tweets, media_formats = "images"):
    '''
        Fetches the media URLs from downloaded tweets.
    '''

    print('\nCollecting Media URLs.....')
    tweets_with_media = set()

    for tweet in all_tweets:
        media = tweet.entities.get('media',[])
        if len(media) > 0:
            # print(media)
            if media_formats == "all":
                tweets_with_media.add(media[0]['media_url_https'])
            else:
                if media[0]['media_url_https'].split(".")[-1] in MEDIA_FORMATS[media_formats]:
                    tweets_with_media.add(media[0]['media_url_https'])

            sys.stdout.write("\rMedia Links fetched: %d" % len(tweets_with_media))
            sys.stdout.flush()

    print ('\nFinished fetching ' + str(len(tweets_with_media)) + ' links.')
    return tweets_with_media

def downloadFiles(media_url, username):
    '''
        Downloads the fetched media URLs.
    '''

    print ('\nDownloading Images.....')

    try:
        os.mkdir('twitter_images')
        os.chdir('twitter_images')
    except:
        os.chdir('twitter_images')

    try:
        os.mkdir(username)
        os.chdir(username)
    except:
        os.chdir(username)

    for url in media_url:
        wget.download(url)


def authenticate():
    ''' Authenticate the use of twitter API '''
    auth = OAuth2BearerHandler(tokens.BEARER_TOKEN)
    api = API(auth)
    return api


if __name__ == '__main__':
    main()
