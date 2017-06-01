'''
* @What Data Mining Final Project : Using Tweeter sentiment analysis to predict change in stock price.
* @Author Sabastian Mugazambi & Simon Orlovsky
* @Date 05/27/2017
* @Purpose : Use KNN to predict the change in stock price.
'''
import math
import numpy as np
def euclidean(train,newpoint,k):
    """
    @Function :  euclidean(k,train,newpoint)
    @Args: <k> <training data set points> <the new point to predict change>
    @Purpose: find average changes from knearest neighbors
    """
    cal_dis = list()
    tickers_list = list()
    pec_change = list()

    #Getting the price changes fro the training points
    for key, value in train.iteritems():
        tickers_list.append(value[0])
        y = [value[2],value[3]]
        pec_change.append(value[1])
        #euclidean distance calculation
        cal_dis.append(math.sqrt(np.sum(np.subtract(newpoint,y)**2)))

    voters = np.argsort(cal_dis,axis=-1,kind="mergesort",order=None)
    nearest_stocks = list()
    nearest_pc_changes = list()

    #finding the average of the n neighbors
    for i in range(0,k):
        v = voters[i]
        print pec_change[v]
        if(pec_change[v]!= None):
            nearest_stocks.append(tickers_list[v])
            nearest_pc_changes.append(pec_change[v])
        elif(k==1):
            while(pec_change[v]== None):
                i+=1
                v = voters[i]
            nearest_stocks.append(tickers_list[v])
            nearest_pc_changes.append(pec_change[v])


    print nearest_pc_changes

    return np.mean(nearest_pc_changes)

def run_knn(k,train,newpoint):
    """
    @Function :  run_knn(k,train,newpoint)
    @Args: <k> <training data set points> <the new point to predict change>
    @Purpose: makes call to the euclidean distance method of finding KNN
    """
    return euclidean(train,newpoint,k)
