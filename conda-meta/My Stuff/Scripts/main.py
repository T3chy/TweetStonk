import requests
import tweepy
import datetime
import csv
import pandas as pd
import pandas_datareader.data as web
consumer_key = "wBlchO1ZEiGnv1ly1wmVplNr5"
consumer_secret = "iyHcmJITDblWRf4Zj46r19UVbngnU8DoXkBoXCtchZpZ7kF6HT"
access_key = "1214224530341629952-RpXwF26MvZ0KEBJTcYzwEhKHgE4vQx"
access_secret = "GTa4it7WQ4pXnvu1klWlFnbMFfUSVVBw8gvu0sipWGeD7"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\conda-meta\My Stuff\Data"
def get_tweets(username):
    tmp = []
    for tweet in api.user_timeline(screen_name = username,count=200):
        if not tweet.retweeted:
                if not "RT @" in tweet.text:
                    tmp.append(tweet)
    outtweets = [[(tweet.created_at).strftime('%m/%d/%Y'), tweet.text.encode("utf-8")] for tweet in tmp]
    dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\conda-meta\My Stuff\Data" + "/" + username + "_tweets" + ".txt" 
    with open(dir, 'w') as f:
	    writer = csv.writer(f)
	    writer.writerow(["created_at","text"])
	    writer.writerows(outtweets)
def get_stonks(ticker):
    pass
class company():
    def __init__(self,ticker,twitter):
           self.ticker = ticker
           self.twitter = twitter
    def main(self):
        get_tweets(self.twitter)
c = company('voo','realdonaldtrump')        
c.main()