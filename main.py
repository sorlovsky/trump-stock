'''
* @What Data Mining Final Project : Using Tweeter sentiment analysis to predict change in stock price.
* @Author Sabastian Mugazambi & Simon Orlovsky
* @Date 05/27/2017
* @Purpose : Analyses a tweet and predicts the effect of the tweet on the mentioned company stock price.
* @ test : python main.py 2 F realDonaldTrump 'Totally biased @NBCNews went out of its way to say that the big announcement from Ford, G.M., Lockheed & others that jobs are coming back...' 2017-01-18
'''
#import libraries
import tweepy #https://github.com/tweepy/tweepy
import csv
import random
import numpy as np
import heapq
import math
import collections
from collections import defaultdict
import time
import copy
import sys
import scipy.stats
import nltk
import matplotlib.pyplot as plt
import pylab
import quandl
quandl.ApiConfig.api_key = "mwbHy7C9x4U5HWdxhM9i"

import matplotlib.pyplot as plt
import pandas
import datetime
import urllib2

#importing our files
from tweet_dumper import *
from prediction_knn import *
# from sentiment_analysis import *
word_features = 0

def load_training(filename):
    """
    @Function :  load_training(filename)
    @Args: <filename>
    @Purpose: Takes a training file name csv
    """
    pos = []
    neg = []
    with open(filename, 'rU') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    for pair in content:
        pair = pair.split(",\\t")

        if(pair[1] == 'positive'):
            pos.append((pair[0],pair[1]))
        else:
            neg.append((pair[0],pair[1]))

    return (pos,neg)


    # all_tweets = np.loadtxt(filename,dtype=str,delimiter=",")
    # print all_tweets

def tokenize(pos_tweets, neg_tweets):
    """
    @Function :  tokenize(pos_tweets, neg_tweets)
    @Args: <positive tweets> <negative tweets>
    @Purpose: takes positive and negative tweets and tokenizes them
    """
    tweets = []
    for (words, sentiment) in pos_tweets + neg_tweets:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        tweets.append((words_filtered, sentiment))
    return tweets

def get_words_in_tweets(tweets):
    """
    @Function :  get_words_in_tweets(tweets)
    @Args: <tweets>
    @Purpose: Takes tweets and gets word features
    """
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    """
    @Function :  get_word_features(wordlist)
    @Args: <wordlist>
    @Purpose: Takes a list of words and converts it into feature list
    """
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def extract_features(document):
    """
    @Function :  extract_features(document)
    @Args: <document>
    @Purpose: Takes an entire documents of words and returns frequency distribution
    """
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains: %s' % word] = (word in document_words)
    return features


def get_price(ticker, date):
    try:
        before = date
        before -= datetime.timedelta(days=1)
        data = quandl.get('WIKI/'+ticker, start_date=before, end_date=date)
        # old = data["Close"][0]
        new = data["Close"][1]
        return new

    except:
        pass

def three_day(ticker, date):
    try:
        after = date
        before = date
        after += datetime.timedelta(days=1)
        before -= datetime.timedelta(days=1)
        data = quandl.get('WIKI/'+ticker, start_date=before, end_date=after)
        old = data["Close"][0]
        new = data["Close"][1]

        percent_change = (old - new)/old
        return percent_change

    except:
        pass

# three_day(ticker)
def get_training_stock():
    dict_train = defaultdict(list)
    with open('stock_tweets.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        counter = 0
        for row in spamreader:
            date_split = row[0].split('-')
            d = datetime.date(int(date_split[0]), int(date_split[1]), int(date_split[2]))
            dict_train[row[1]].append(row[2])
            dict_train[row[1]].append(three_day(row[2], d))
    return dict_train

def main():
    """
    @Function :  Main
    @Args: None <uses sys.argv>
    @Purpose: function and user interface of this program
    """
    global word_features
    #getting the argments
    pred_k = int(sys.argv[1])
    c_symbol = sys.argv[2]
    person = sys.argv[3]
    tweet = sys.argv[4]
    date = sys.argv[5]
    date_split = date.split('-')
    date = datetime.date(int(date_split[0]), int(date_split[1]), int(date_split[2]))

    # STEP 1 : Get and dumb tweets
    #get_all_tweets(person)

    # STEP 2 : Create training sets
    train_data = load_training("training_tweets.csv")

    # STEP 3 : torkenize training data set tweets
    tweets = tokenize(train_data[0], train_data[1])

    # STEP 4 : Feature extraction from the training set
    word_features = get_word_features(get_words_in_tweets(tweets))
    training_set = nltk.classify.apply_features(extract_features, tweets)

    #STEP 5 : classify the given tweet as positive or negative sentiment
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    pred_directional_change =  classifier.classify(extract_features(tweet.split()))
    newpoint = []
    newpoint.append(classifier.prob_classify(extract_features(tweet.split())).prob('positive'))
    newpoint.append(classifier.prob_classify(extract_features(tweet.split())).prob('negative'))

    #print out the sentiment
    print "\n------------------------"
    print "\nThe tweet is:\n"," '",tweet,"'"
    print "\n------------------------"
    print "\nPredicted Sentiment Classification :", pred_directional_change
    print "\n------------------------"

    # Step 6
    train =  get_training_stock()
    for key, value in train.iteritems():
        pred_directional_change =  classifier.classify(extract_features(key.split()))
        train[key].append(classifier.prob_classify(extract_features(key.split())).prob('positive'))
        train[key].append(classifier.prob_classify(extract_features(key.split())).prob('negative'))

    percentage_change =  run_knn(pred_k,train,newpoint)

    print "\nPredicted Pecentage Change in Price :", percentage_change
    print "\n------------------------"

    #STEP 7 Calculate predicted price EOD

    opening_price = get_price(c_symbol,date)
    pred_price = opening_price * (1+percentage_change)
    # if(pred_directional_change == "negative"):
    #     pred_price = opening_price * (1-percentage_change)
    # else:
    #     pred_price = opening_price * (1+percentage_change)


    print "\nPredicted Price Due to Tweet:", pred_price
    print "\n------------------------"

if __name__ == '__main__':
    main()
