'''
* @What Data Mining Final Project : Using Tweeter sentiment analysis to predict change in stock price.
* @Author Sabastian Mugazambi & Simon Orlovsky
* @Date 05/27/2017
* @Purpose : Analyses a tweet and predicts the effect of the tweet on the mentioned company stock price.
'''

List of Files
_____________

1. main.py - main file to run
2. tweet_dumper.py - gets tweets to be used / already done for you
3. stock_prices.py - gets stock prices
4. prediction_knn.py - predicts the price change using knn
5. get-pip.py - Used for installing pip

csv files are used for data import.

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
_________________

- In the command line terminal navigate to the directory where the files exists
	Run main.py as follows:

	$ python main.py <k> <Company Ticker> <Twitter UserID> <Tweet Text> <Date>

  Parameters Explained
  ____________________

  <k> : The number of nearest neighbors to used predict price change
  <Company Ticker>  : Official stock exchange ticker symbol
  <Twitter UserID>  : The official UserID of the individual tweeting
  <Tweet Text>  : The tweet text with the company mentioned in quotes
  <Date>  : Date of the tweet in the format YYYY-DD-MM with no quotes

  Example
  ____________________

  $ python main.py 5 F realDonaldTrump 'Totally biased @NBCNews went out of its way to say that the big announcement from Ford, G.M., Lockheed & others that jobs are coming back...' 2017-01-18


Output Explained
_________________

➜  $ main.py 5 F realDonaldTrump 'Totally biased @NBCNews went out of its way to say that the big announcement from Ford, G.M., Lockheed & others that jobs are coming back...' 2017-01-18

------------------------
<Displays the tweet entirely>

The tweet is:
 ' Totally biased @NBCNews went out of its way to say that the big announcement from Ford, G.M., Lockheed & others that jobs are coming back... '

------------------------
<Displays the predicted sentiment of the tweet understood as the effect it has
on stock price >

Predicted Sentiment Classification : negative

------------------------
<Displays the predicted percentage change in price>

Predicted Percentage Change in Price : 0.00819809018105

------------------------
<Displays the predicted price EOD of the company in question and the actual EOD of that day>

Predicted Price Due to Tweet: 12.5066220828

Actuall EOD Price: 12.41

------------------------

Have fun!
