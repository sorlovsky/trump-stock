
'''
* @What Data Mining Final Project : Using Tweeter sentiment analysis to predict change in stock price.
* @Author Sabastian Mugazambi & Simon Orlovsky
* @Date 05/27/2017
* @Purpose : Collects all the tweets from a given user name and dumps them in csv file.
'''
#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "917YwkktnGtrCjt7DSqshcbBh"
consumer_secret = "OyKlZLwUl96ahrmSe3UIyUBrMWcdKmGbGh9Ogf1bKomQIPazEF"
access_key = "242109824-FEL2qiVcPm7dYQZitG7szAaXK9oz9fqGiVUSNFxf"
access_secret = "8hYzrUpnpmVXRpdW40eMqdGusudo6ItfDOE2Alk1Tkd9o"


def get_all_tweets(screen_name):
    """
    @Function :  get_all_tweets(screen_name)
    @Args: <user name>
    @Purpose: gets all the tweets of given user id
    """
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))

    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    #write the csv
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

    pass
