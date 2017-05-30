import quandl
quandl.ApiConfig.api_key = "mwbHy7C9x4U5HWdxhM9i"

import matplotlib.pyplot as plt
import pandas
import numpy
import nltk
import datetime
import urllib2

# date = "2017-3-28"
d = datetime.date(2017, 3, 28)
after = d
before = d
after += datetime.timedelta(days=1)
before -= datetime.timedelta(days=1)
ticker = 'TM'

# print(d)

def three_day():
	try:
		data = quandl.get('WIKI/'+ticker, start_date=before, end_date=after)
		old = data["Close"][0]
		new = data["Close"][1]

		percent_change = (old - new)/old
		print(percent_change)

	except:
		print "Data not available in WIKI stock data or incorrect ticker."


