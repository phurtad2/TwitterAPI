import json
import pandas as pd
import re
import matplotlib.pyplot as plt
from itertools import islice
import random
atoken = ''
asecret = ''
ckey = ''
csecret= ''


tweets_data_path = 'twitter_data.txt'
tweets_data = []

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def randomColor():
    return (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))


tweets_file = open(tweets_data_path, "r+")
datapts = [0, 0]
keywords = ["", ""]
colors = [rgb_to_hex(randomColor()), rgb_to_hex(randomColor())]
count = 0

for line in islice(tweets_file, 0, 2):
    keywords[count] = line.strip()
    count += 1

for line in tweets_file:
    try:
        tweet = json.loads(line)
        print(tweet['text'])
        for i in range(0, len(datapts)):
            datapts[i] += 1 if word_in_text(keywords[i], str(tweet)) else 0
        tweets_data.append(tweet)
    except:
        continue

total = len(tweets_data)
plt.xlabel('Queries')
plt.ylabel("# of Tweets")
plt.title("Tweet Comparison: " + keywords[0] + " vs. " + keywords[1])


xcoords = [i + 0.1 for i in range(0, len(keywords))]

plt.bar(xcoords,datapts, color=colors)

plt.xticks([i + 0.5 for i in range(0, len(keywords))], keywords)
plt.ylim([0,len(tweets_data)])
print("Final Results")
print("-------------------------------------------")
print(keywords)
print(datapts)
print("Total: " + str(total))
print(keywords[0].strip() + ": " + str(datapts[0]) + " Tweets")
print(keywords[1].strip() + ": " + str(datapts[1]) + " Tweets")
plt.show()
