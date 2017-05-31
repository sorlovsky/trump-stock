import quandl
quandl.ApiConfig.api_key = "mwbHy7C9x4U5HWdxhM9i"

import matplotlib.pyplot as plt
import pandas
import numpy
import nltk
import datetime
import urllib2
import csv

# date = "2017-3-28"
d = datetime.date(2017, 3, 28)

# ticker = 'F'

# print(d)

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
		print "Data not available in WIKI stock data or incorrect ticker: ", ticker

def one_day(ticker):

# three_day(ticker)

with open('stock_tweets.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	counter = 0
	for row in spamreader:
		date_split = row[0].split('-')
		d = datetime.date(int(date_split[0]), int(date_split[1]), int(date_split[2]))
		print three_day(row[2], d), row[2]
		# print row[2]
