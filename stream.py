

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import time
import json
import pprint
from collections import defaultdict
import re
import urllib2




API_KEY = 'De2sW3frPrzjNCj7ov8OzufYM'
API_SECRET_KEY = 'KfF50W83f1hQ4bwOJqkMpmtTT1wdFz4BsiCNVy3Ljztb0XyIqQ'
ACCESS_TOKEN = '3278358554-JIN2xfjgSprx1SiGFVaFr4ahgqgCMFdlnEOZCXn'
ACCESS_TOKEN_SECRET = 'A1Z1BMeZQQLYVvjeGWyM8jChxhm7hD1CPy87h9ry828d4'

tweets = defaultdict(list)
name = {}

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

myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(time_limit=5))
myStream.filter(track=['government'])





with open('abcd.json') as f:
    content = f.readlines()

for i in content:
    data = json.loads(i)
    
    tweets[data['user']['id']].append(data['text'])
    name[data['user']['id']] = data['user']['name']




print(tweets)
print("\n")
print(name)


for id,tweet in tweets.items():
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet)
    for url in urls:
        try:
            res = urllib2.urlopen(url)
            actual_url = res.geturl()
            print(actual_url)
        except:
            print(url)











# you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content] 

# Splitting the data and converting to list
# scrap = content[0][1:]
# scrap_list = scrap[:-1].split(",")

# print(content[0])

# flag = -1
# # Converting into Dictionary
# for entry in range(0, len(scrap_list)):
#     key = scrap_list[entry].split(":")[0]
    
#     if key == "\"indices\"":
#         flag = entry + 1
#         continue

#     if flag == entry:
#         continue

#     value = scrap_list[entry].split(":")[1]
#     Tweet_Info[key] = value

# print(Tweet_Info)
