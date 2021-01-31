import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import time
import json
import pprint
from collections import defaultdict
import re
import requests
from collections import Counter





API_KEY = 'De2sW3frPrzjNCj7ov8OzufYM'
API_SECRET_KEY = 'KfF50W83f1hQ4bwOJqkMpmtTT1wdFz4BsiCNVy3Ljztb0XyIqQ'
ACCESS_TOKEN = '3278358554-JIN2xfjgSprx1SiGFVaFr4ahgqgCMFdlnEOZCXn'
ACCESS_TOKEN_SECRET = 'A1Z1BMeZQQLYVvjeGWyM8jChxhm7hD1CPy87h9ry828d4'

tweets = defaultdict(list)
name = {}
url_dict = {}
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

class MyStreamListener(tweepy.StreamListener):
	def __init__(self, time_limit=60):
		self.start_time = time.time()
		self.limit = time_limit
		open("abcd.json", "w").close()
		self.saveFile = open('abcd.json', 'a')
		super(MyStreamListener, self).__init__()

	def on_data(self, data):
		if (time.time() - self.start_time) < self.limit:
			self.saveFile.write(data)
			# self.saveFile.write('\n')
			return True
		else:
			self.saveFile.close()
			return False


auth = OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



report = 1
input_word = str(input("Enter the Keyword : "))
input_list = []
input_list.append(input_word)
while(1):
	print("\n\n*************************************Last 1 Minute Report ","************************************")




	print("\n\n ------------------------User Report---------------------------- \n")
	f_task= open("Task_1/Task_1.txt","a+")
	f_task.write("\n\n****************************************************************************Last 1 Minute Report *********************************************************************************")
	f_task.write("\n\n-------------------------------------------------User Report------------------------------------------------")



	report = report + 1

	myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(time_limit=5))
	myStream.filter(track=input_list)

	with open('abcd.json') as f:
		content = f.readlines()



	twitter_id = []
	for i in content:
		data = json.loads(i)
		twitter_id.append(data['user']['id'])
		tweets[data['user']['id']].append(data['text'])
		name[data['user']['id']] = data['user']['name']




	f_task.write("\n\nTwitter User Name  ------------------------------------------------------------------- Twitter Counts\n")
	print("Twitter User Name        --------------------------------------------- Twitter Counts")
	for id in twitter_id:
		print(name[id]," ",len(tweets[id]))
		f_task.write("\n"+str(name[id])+"   :    "+str(len(tweets[id])))




	for id,tweet in tweets.items():
		for text in tweet:
			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
			for url in urls:
				try:
					site = requests.get(url)

					if site.url in url_dict:
						url_dict[site.url] = url_dict[site.url] + 1
					else:
						url_dict[site.url] = 1

				except:
					pass
					# url_dict[data['user']['id']].append(url)







	print("\n\n ------------------------------Links Report---------------------------- \n")

	f_task.write("\n\n ------------------------Links Report---------------------------- \n")

	url_unique = 0
	for key, value in url_dict.items():
		if value == 1:
			url_unique = url_unique + 1

	


	f_task.write("Unique Url is : "+str(url_unique))
	print("Unique Url is ",url_unique)

	print("Total Url Links ",len(url_dict))
	f_task.write("\nTotal Url Links "+str(url_unique))

	unique_url = Counter(dict(sorted(url_dict.items(), key=lambda item: item[1])))

	print("\n\nURL        :          Url Count\n")
	f_task.write("\n\nURL        :          Url Count\n")
	for key, value in unique_url.items():
		print(key,"     :       ",value)
		f_task.write(str(key)+"        :          "+str(value)+"\n")



	f_task.write("\n\n ------------------------Content Report---------------------------- \n")
	print("\n\n -------------------------------Content Report---------------------------- \n")

	twitter_combine = ""
	for id,tweet in tweets.items():
		for text in tweet:
			twitter_combine = twitter_combine + " "+text


	tweet_list = twitter_combine.split()
	final_tweet_list = []
	for tweet in tweet_list:
		if tweet not in stop_words:
			final_tweet_list.append(tweet)



	tweet_count = Counter(final_tweet_list)

	unique_word_count = 0
	for key,val in tweet_count.items():
		if val == 1:
			unique_word_count = unique_word_count + 1


	print("\nUnique Word Count Is ",unique_word_count)

	dict(sorted(tweet_count.items(), key=lambda item: item[1]))

	Top10_Occurence = sorted(tweet_count, key=tweet_count.get, reverse=True)[:10]
	print("\nTop 10 Occurence is ",Top10_Occurence)

	
	twitter_id.clear()
	tweets.clear()
	name.clear()
	url_dict.clear()
	final_tweet_list.clear()
	tweet_count.clear()











