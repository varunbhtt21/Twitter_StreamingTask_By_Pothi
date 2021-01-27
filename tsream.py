import tweepy

# from shh.keys import*

API_KEY = 'De2sW3frPrzjNCj7ov8OzufYM'
API_SECRET_KEY = 'KfF50W83f1hQ4bwOJqkMpmtTT1wdFz4BsiCNVy3Ljztb0XyIqQ'
ACCESS_TOKEN = '3278358554-JIN2xfjgSprx1SiGFVaFr4ahgqgCMFdlnEOZCXn'
ACCESS_TOKEN_SECRET = 'A1Z1BMeZQQLYVvjeGWyM8jChxhm7hD1CPy87h9ry828d4'

#Create a Stream Listener

class MaxListener(tweepy.StreamListener):

	def on_data(self, raw_data):
		self.process_data(raw_data)

		return True


	def process_data(self, raw_data):
		print(raw_data)


	def on_error(self, status_code):
		if status_code == 420:
			return False



# Create a Stream
class MaxStream():

	def __init__(self, auth, listener):
		self.stream = tweepy.Stream(auth=auth, listener=listener)

	def start(self, keyword_list):
		self.stream.filter(track=keyword_list)


# Start the Stream

if __name__ == "__main__":
	listener = MaxListener()

	auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	stream = MaxStream(auth, listener)
	stream.start(['shahrukh khan'])