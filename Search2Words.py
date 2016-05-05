from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import os

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '3433403097-HlLrdLubHDlVLHT0fcox275EIjcv6Oh5wyEXI63'
ACCESS_SECRET = 'iC0Kg69aS05faFU4sF864e0WSgkAHGKgzs8NBnOdHh3yT'
CONSUMER_KEY = 'lQ5XEKtDycBVlrvYmc75oOl9C'
CONSUMER_SECRET = 'eGAdoxsmc6MoTUUHLeLHow6f7SoUeqzEicrjw9piqmxOPgHHJG'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)
        bool = True
        if 'text' in tweet:
            str = tweet['text'].encode('ascii', 'replace').decode()
            print(str)
            with open('twitter_data.txt','a') as tf:
                tf.write(data)
                size = os.path.getsize("/home/patrick/PycharmProjects/TwitterAPI/twitter_data.txt")
                if size > ((1000000)*20): #20 Megabytes
                    bool = False
                return bool





    def on_error(self, status):
        print("error")
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    name1 = input("Enter first query: ")
    name2 = input("Enter second query: ")
    print(name1 + " vs. " + name2)

    print("--------------------------------\n")
    f = open("twitter_data.txt", "w")
    f.write(name1 + '\n')
    f.write(name2 + '\n')

    stream.filter(track=[name1, name2], languages=["en"])
    print("Maximum Size Reached")
