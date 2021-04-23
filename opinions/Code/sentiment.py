import requests
import json
import tweepy
import jsonpickle as js

def sentiment(query, numTweets):
	#file = open('debug.txt', 'w')
	#file.truncate()

	CKEY = 
	CSCRT = 
	auth = tweepy.OAuthHandler(CKEY, CSCRT)

	try:
		redirect_url = auth.get_authorization_url()
	except tweepy.TweepError:
		pass # How am I even SUPPOSED to handle this?!
		#print("'Error: Can't obtain request token.")

	ATKN = 
	ASCRT = 

	auth.set_access_token(ATKN, ASCRT)

	api = tweepy.API(auth)

	counter = 0

	tweets = []

	for status in tweepy.Cursor(api.search, q=query).items(numTweets):
		if len(tweets) < numTweets:
			tweets.append(js.encode(status, unpicklable = True))

	tweetlist = []

	##print(tweets)
	##print('''
	#	-------------------------------------------------------------------
	#	''')
	txt = js.encode(tweets, unpicklable = False)
	##print(txt)
	split = txt.split(',')

	for i in split:
		i = i.strip()

		if '}' in i:
			i.replace('}', '')

		if i.startswith('\\"text\\"') and i[9:] not in tweetlist and i[:-1] not in tweetlist and i[9:-1] not in tweetlist: #I wrote this some time
			counter += 1#                                                                                                   ago and I can't be
#                                                                                                                           bothered to fix it			
			if i.endswith('''"'''):
				i = i [:-1]
			
			#print(counter, ':', i[9:])
			tweetlist.append(i[9:])

	##print(tweetlist)

	dic = {'data': []}

	for i in range(len(tweetlist)):
		tweet = tweetlist[i]
		#file.write('\nTweet ' + str(i) + ': ' + tweet)
		if '\\' in tweet:
			modTweet = tweet.replace('\\', '')
			#file.write('\n(rep) Tweet ' + str(i) + ': ' + modTweet)
		dic['data'].append({'text': modTweet, 'query':query})

	url = 'http://www.sentiment140.com/api/bulkClassifyJson'

	r = requests.post(url, data = json.dumps(dic))

	polarities = json.loads(r.text)
	##print(polarities)

	final = []

	for dat in polarities['data']:
		final.append(dat['polarity'])
		##print(dat['text'])

	##print(final)

	#print(sum(final)/len(final))

	final2 = []
	for i in final:
		if i != 2:
			final2.append(i)

	#print(final2)
	try:
		percentage = (sum(final2)/len(final2)/(4/100))
	except ZeroDivisionError:
		percentage = 50
	positive = final2.count(4)
	negative = final2.count(0)
	neutral = final.count(2)

	return {'positive':positive, 'negative':negative, 'neutral':neutral, 'percentage':percentage}

if __name__ == "__main__":
	x = input('Query:')
	y = int(input('No. Of Tweets:'))

	print(sentiment(x, y))
