'''
* @What Data Mining Final Project : Using Tweeter sentiment analysis to predict change in stock price.
* @Author Sabastian Mugazambi & Simon Orlovsky
* @Date 05/27/2017
* @Purpose : Analyses a tweet and predicts the effect of the tweet on the mentioned company stock price.
'''

List of Files
_____________

1. main.py - main file to run
2. tweet_dumper.py - gets tweets to be used
3. stock_prices.py - gets stock prices
4. prediction_knn.py - predicts the price change using knn
5. get-pip.py - Used for installing pip

Dependencies
_____________

There are a couple of libraries that our code relies on and it is essential to have these libraries installed before running the program.

- Tweepy :
          1. install pip using the command line
              $ sudo python get-pip.py
          2. install Tweepy
              $ sudo pip install --ignore-installed tweepy

- Quandl :
          1. install Quandl
              $ sudo pip install --ignore-installed quandl

Make sure that these dependencies are installed for successfully running the
main program.

Running the main
_____________

- In the command line terminal navigate to the directory where the files exists
	Run knn-cv.py as follows:

	$ python knn-cv.py {k} {distance}

e.g python knn-cv.py 3 euclidean
e.g python knn-cv.py 5 manhattan


2. Printing out confusion matrix

- I implemented a method that prints out the confusion matrix but the columns and
	rows are not labeled. However they follow the following ocnvention.

				   Predicted
                 1     2     7
        	1 100.0   0.0   0.0
Actual      2  10.0  85.0   5.0
            7   5.0   0.0  95.0

Note that for tie breaking I choose the first element with the highest votes which is basically a random way of dealing with tie breaking.
