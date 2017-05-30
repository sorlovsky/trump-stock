'''
* @What Data Mining Final Project : Using Tweeter sentiment analysis to predict change in stock price.
* @Author Sabastian Mugazambi & Simon Orlovsky
* @Date 05/27/2017
* @Purpose : Use KNN to predict the change in stock price.
'''

def euclidean(k,train,newpoint):
    """
    @Function :  euclidean(k,train,newpoint)
    @Args: <k> <training data set points> <the new point to predict change>
    @Purpose: find average changes from knearest neighbors
    """
	cal_dis = list()
    tickers_list = list()
    pec_change = list()

	for key, value in d.iteritems():
        tickers_list.append(key)
        y = value[0]
        pec_change = value[1]
		cal_dis.append(math.sqrt(np.sum(np.subtract(newpoint,y)**2)))

	voters = np.argsort(cal_dis,axis=-1,kind="mergesort",order=None)
	nearest_stocks = list()
    nearest_pc_changes = list()

	for i in range(0,k):
        v = voters[i]
		nearest_stocks.append(tickers_list[v])
        nearest_pc_changes.append(pec_change[v])

	return np.mean(nearest_stocks)

def run_knn(k,train,newpoint):
    """
    @Function :  run_knn(k,train,newpoint)
    @Args: <k> <training data set points> <the new point to predict change>
    @Purpose: makes call to the euclidean distance method of finding KNN
    """
    return euclidean(train,newpoint,k))
