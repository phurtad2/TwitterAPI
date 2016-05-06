try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
atoken = '3433403097-HlLrdLubHDlVLHT0fcox275EIjcv6Oh5wyEXI63'
asecret = 'iC0Kg69aS05faFU4sF864e0WSgkAHGKgzs8NBnOdHh3yT'
ckey = 'lQ5XEKtDycBVlrvYmc75oOl9C'
csecret = 'eGAdoxsmc6MoTUUHLeLHow6f7SoUeqzEicrjw9piqmxOPgHHJG'

oauth = OAuth(atoken, asecret, ckey, csecret)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)
twitter = Twitter(auth=oauth)
# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
tweet_count = 10
# for tweet in iterator:
#    tweet_count -= 1
# Twitter Python Tool wraps the data returned by Twitter
# as a TwitterDictResponse object.
# We convert it back to the JSON format to print/score


# The command below will do pretty printing for JSON data, try it out
#    if 'text' in tweet:
#        print(json.dumps(tweet['text'], indent=4))
#    print("----------------------------------")
#    if tweet_count <= 0:
#        break
tweety = twitter.statuses.user_timeline(screen_name="himynameismads", count=150)
k = 0
for i in tweety:
    print(json.dumps(tweety[k]['text'], indent=4))
    k += 1
