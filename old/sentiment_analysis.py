import nltk

# pos_tweets = [('Big win in Montana for Republicans!', 'positive'),
#                   ('Thank you to Ford for scrapping a new plant in Mexico and creating 700 new jobs in the U.S. This is just the beginning - much more to follow', 'positive'),
#               ('I feel great this morning', 'positive'),
#               ('I am so excited about the concert', 'positive'),
#               ('He is my best friend', 'positive')]
#
# neg_tweets = [('With all of the illegal acts that took place in the Clinton campaign & Obama Administration, there was never a special counsel appointed', 'negative'),
#               ('This view is horrible', 'negative'),
#               ('I feel tired this morning', 'negative'),
#               ('I am not looking forward to the concert', 'negative'),
#               ('He is my enemy', 'negative')]
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

word_features = get_word_features(get_words_in_tweets(tweets))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains: %s' % word] = (word in document_words)
    return features

# training_set = nltk.classify.apply_features(extract_features, tweets)
# classifier = nltk.NaiveBayesClassifier.train(training_set)
# tweet = 'Clinton'
# print classifier.classify(extract_features(tweet.split()))
