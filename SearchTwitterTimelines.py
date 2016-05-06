try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
atoken = ''
asecret = ''
ckey = ''
csecret = ''

oauth = OAuth(atoken, asecret, ckey, csecret)

# Initiate the connection to Twitter Streaming API
twitter = Twitter(auth=oauth)

screen_name = input("Enter Username of Interest: ")
count = input("Enter number of tweets requesting: ")
tweets = twitter.statuses.user_timeline(screen_name=screen_name, count=count)
k = 0
for i in tweets:
    print(str(k+1) + ". " + json.dumps(tweets[k]['text'], indent=4))
    k += 1
