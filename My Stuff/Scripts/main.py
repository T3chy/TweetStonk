import requests
import tweepy
from datetime import datetime, timedelta, date
import csv
import pandas as pd
import re
from pandas_datareader import data
consumer_key = "wBlchO1ZEiGnv1ly1wmVplNr5"
consumer_secret = "iyHcmJITDblWRf4Zj46r19UVbngnU8DoXkBoXCtchZpZ7kF6HT"
access_key = "1214224530341629952-RpXwF26MvZ0KEBJTcYzwEhKHgE4vQx"
access_secret = "GTa4it7WQ4pXnvu1klWlFnbMFfUSVVBw8gvu0sipWGeD7"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data"
def get_tweets(username):
    global tmp
    tmp = []
    for tweet in api.user_timeline(screen_name = username,count=200):
        if not tweet.retweeted:
                if not "RT @" in tweet.text:
                    tmp.append(tweet)
    outtweets = [[(tweet.created_at).strftime('%m/%d/%Y'), tweet.text.encode("utf-8")] for tweet in tmp]
    dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data" + "/" + username + "_tweets" + ".csv" 
    with open(dir, 'w') as f:
	    writer = csv.writer(f)
	    writer.writerow(["created_at","text"])
	    writer.writerows(outtweets)
def get_stonks(ticker):
 #   LastDateRegex = re.compile(r'/(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.](19|20)\d\d/') 
 #   mo = LastDateRegex.search()
     print(data.DataReader(ticker, 
                       start=((tmp[-1].created_at)- timedelta(days=1)).strftime('%m/%d/%Y'), 
                       end=((date.today())+timedelta(days=1)), 
                       data_source='yahoo')['Close'])
class company():
    def __init__(self,ticker,twitter):
           self.ticker = ticker
           self.twitter = twitter
    def main(self):
        get_tweets(self.twitter)
        get_stonks(self.ticker)
c = company('voo','realdonaldtrump')        
c.main()