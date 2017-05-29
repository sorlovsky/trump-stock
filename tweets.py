from nltk.tokenize import sent_tokenize, word_tokenize


positive_tweets = 

negative_tweets = 

tweets = [
 	(['illegal', 'acts', 'place', 'Clinton', 'campaign', 'Obama', 'Administration', 'never', 'special', 'counsel', 'appointed!'], 'negative'),
    (['Big', 'win', 'in', 'Montana', 'republicans'], 'positive') 
	(['Thank', 'Ford', 'scrapping', 'new', 'plant', 'Mexico', 'creating', 'new', 'jobs', 'U.S.', 'beginning', 'much', 'more', 'follow'], 'positive')
	]


pos_tweets = [('Big win in Montana for Republicans!'),
			  ('Thank you to Ford for scrapping a new plant in Mexico and creating 700 new jobs in the U.S. This is just the beginning - much more to follow')]

neg_tweets = [
			('With all of the illegal acts that took place in the Clinton campaign & Obama Administration, there was never a special counsel appointed!')]
			  
# word_tokenize('Big win in Montana for Republicans!')
# tweets = [(['big', 'win', 'in', 'Montanta', 'Republicans'], 'positive')]
# ('Getting', 'ready', 'to', 'leave', 'Great', 'State', 'Indiana', 'meet', 'hard', 'working' and wonderful people of Carrier A.C.', 'positive'),

# ('Just watched the totally biased and fake news reports of the so-called Russia story on NBC and ABC. ', 'negative'),

