# Grap multiple user's user_timeline from twitter API and save to Excel
# Code will be save user's tweet ID, created Time, Coordinates-x, Coordinates-y, source, text. Can be modified at line 48 and so on
# Original code from https://gist.github.com/yanofsky/5436496  "A script to download all of a user's tweets into a csv"

import xlsxwriter
import tweepy

#https://github.com/tweepy/tweepy

consumer_key = "917YwkktnGtrCjt7DSqshcbBh"
consumer_secret = "OyKlZLwUl96ahrmSe3UIyUBrMWcdKmGbGh9Ogf1bKomQIPazEF"
access_key = "242109824-FEL2qiVcPm7dYQZitG7szAaXK9oz9fqGiVUSNFxf"
access_secret = "8hYzrUpnpmVXRpdW40eMqdGusudo6ItfDOE2Alk1Tkd9o"

def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []
    new_tweets = []
    outtweets = []

    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))

    #transform the tweepy tweets into a 2D array
    outtweets = [[tweet.id_str, tweet.created_at, tweet.coordinates,tweet.geo,tweet.source,tweet.text] for tweet in alltweets]

    return outtweets

def write_worksheet(twitter_name):

	#formating for excel
	format01 = workbook.add_format()
	format02 = workbook.add_format()
	format03 = workbook.add_format()
	format04 = workbook.add_format()
	format01.set_align('center')
	format01.set_align('vcenter')
	format02.set_align('center')
	format02.set_align('vcenter')
	format03.set_align('center')
	format03.set_align('vcenter')
	format03.set_bold()
	format04.set_align('vcenter')
	format04.set_text_wrap()

	out1 = []
	header = ["id","created_at","coordinates-x","coordinates-y","source","text"]

	worksheet = workbook.add_worksheet(twitter_name)

	out1 = get_all_tweets(twitter_name)
	row = 0
	col = 0

	worksheet.set_column('A:A', 20)
	worksheet.set_column('B:B', 18)
	worksheet.set_column('C:C', 13)
	worksheet.set_column('D:D', 13)
	worksheet.set_column('E:E', 20)
	worksheet.set_column('F:F', 120)

	for h_item in header:
		worksheet.write(row, col, h_item, format03)
		col = col + 1

	row += 1
	col = 0

	for o_item in out1:
		write = []
		cord1 = 0
		cord2 = 0
		write = [o_item[0], o_item[1], o_item[4], o_item[5]]

		if o_item[2]:
			cord1 = o_item[2]['coordinates'][0]
			cord2 = o_item[2]['coordinates'][1]
		else:
			cord1 = ""
			cord2 = ""

		format01.set_num_format('yyyy/mm/dd hh:mm:ss')
		worksheet.write(row, 0, write[0], format02)
		worksheet.write(row, 1, write[1], format01)
		worksheet.write(row, 2, cord1, format02)
		worksheet.write(row, 3, cord2, format02)
		worksheet.write(row, 4, write[2], format02)
		worksheet.write(row, 5, write[3], format04)
		row += 1
		col = 0

workbook = xlsxwriter.Workbook('Twitter_timeline.xlsx')


write_worksheet('twitterID1')
write_worksheet('twitterID2')

workbook.close()
