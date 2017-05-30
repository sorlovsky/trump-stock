
import numpy as np
import matplotlib.pyplot as plt
import pylab
import sys
import math


def euclidean(k,train,newpoint):

	cal_dis = list()
    tickers_list = list()

	for key, value in d.iteritems():
        tickers_list.append(key)
        y = value[0]
		cal_dis.append(math.sqrt(np.sum(np.subtract(newpoint,y)**2)))

	voters = np.argsort(cal_dis,axis=-1,kind="mergesort",order=None)
	nearest_stocks = list()

	for i in range(0,k):
		nearest_stocks.append(tickers_list[voters[i]])

	return nearest_stocks

def run_knn(k,train,newpoint):
    return euclidean(train,newpoint,k))
