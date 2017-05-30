'''
* @What Data Mining Final Project : Using Tweeter sentiment analysis to predict change in stock price.
* @Author Sabastian Mugazambi & Simon Orlovsky
* @Date 05/27/2017
* @Purpose : Analyses a tweet and predicts the effect of the tweet on the mentioned company stock price.
* @ test : python main.py 2 F realDonaldTrump 'This sucks' 05/27/2017
'''
#import libraries
import tweepy #https://github.com/tweepy/tweepy
import csv
import random
import numpy as np
import heapq
import math
import collections
import time
import copy
import sys
import scipy.stats
import nltk

#importing our files
from tweet_dumper import *
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
    tweets = []
    for (words, sentiment) in pos_tweets + neg_tweets:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        tweets.append((words_filtered, sentiment))
    return tweets

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains: %s' % word] = (word in document_words)
    return features

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

    #print out the sentiment
    print "\n------------------------"
    print "\nThe tweet is:\n"," '",tweet,"'"
    print "\n------------------------"
    print "\nSentiment Classification :", pred_directional_change
    print "\n------------------------"


if __name__ == '__main__':
	main()
