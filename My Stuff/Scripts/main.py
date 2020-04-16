import requests
import tweepy
from datetime import datetime, timedelta, date
import csv
import pandas as pd
import re
from pandas_datareader import data
from textblob import TextBlob
import nltk
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import fixdata
import os
consumer_key = "wBlchO1ZEiGnv1ly1wmVplNr5"
consumer_secret = "iyHcmJITDblWRf4Zj46r19UVbngnU8DoXkBoXCtchZpZ7kF6HT"
access_key = "1214224530341629952-RpXwF26MvZ0KEBJTcYzwEhKHgE4vQx"
access_secret = "GTa4it7WQ4pXnvu1klWlFnbMFfUSVVBw8gvu0sipWGeD7"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data"
tmp = []
class company():
    def __init__(self,ticker,twitter,numtwt):
           self.ticker = ticker
           self.twitter = twitter
           self.numtwt = numtwt
    def get_tweets(self):
        initamount = self.numtwt
        username = self.twitter
        amount = initamount
        global tmp
        tmp = []
        def gather(count):
            for tweet in api.user_timeline(screen_name = username,count=count):
                if not tweet.retweeted:
                        if not "RT @" in tweet.text:
                            if (tweet.created_at).weekday() <= 5:
                                tmp.append(tweet)  
        if initamount <= 200:
            gather(amount)
        else:
            while amount > 0:
                if amount > 200:
                    gather(200)
                    amount = amount - 200
                else:
                    gather(amount)  
        outtweets = [[(tweet.created_at).strftime('%m/%d/%Y'), tweet.text.encode("utf-8")] for tweet in tmp]
        dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data" + "/" + username + "_tweets" + ".csv" 
        with open(dir, 'w') as f:
	        writer = csv.writer(f)
	        writer.writerow(["created_at","text"])
	        writer.writerows(outtweets)
    def Sentimentweet(self):
        username = self.twitter
        dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data" + "/" + username + "_tweets" + ".csv" 
        with open(dir) as csvfile:
            reader = csv.reader(csvfile)
            avg = 0
            num = 0
            tdate = ""
            sentiments = []
            for row in reader:
                if row == []:
                        continue
                if row[0] == "created_at":
                    continue
                tw = TextBlob(str(row[1]))
                if tdate == row[0] or tdate == "":
                    avg = avg + tw.sentiment.polarity
                    num = num + 1
                    tdate = row[0]
                else:                    
                    sentiments.append([tdate,(avg/num)])
                    tdate = row[0]
                    avg = 0
                    num = 0
                    avg = avg + tw.sentiment.polarity
                    num = num + 1
            dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data" + "/" + username + "_polarity" + ".csv" 
            with open(dir, 'w') as f:
	            writer = csv.writer(f)
	            writer.writerow(["Date","Polarity"])
	            writer.writerows(sentiments)      
    def get_stonks(self):
        global tmp
        ticker = self.ticker
        username = self.twitter
        datas = []
        df = data.DataReader(ticker, 
                       start=((tmp[-1].created_at)- timedelta(days=1)).strftime('%m/%d/%Y'), 
                       end=((date.today())+timedelta(days=1)), 
                       data_source='yahoo')
        df.reset_index(inplace=True,drop=False)
        for index, row in df.iterrows():
            datas.append([row['Date'].strftime('%m/%d/%Y'),row['Close']])
        dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data" + "/" + username + "_prices" + ".csv"  
        with open(dir, 'w') as f:
	        writer = csv.writer(f)
	        writer.writerow(["Date","Price"])
	        writer.writerows(datas)
    def main(self):
        company.get_tweets(self)
        company.get_stonks(self)
        company.Sentimentweet(self)
        fixdata.graphem(self.twitter)
#companies = input("how many companies would you like to analyze?")
#for i in range(int(companies)):
 #   companyt = input("Corperate twitter handle?")
 #   ticker = input("stock ticker?")
 #   twtnum = input("how many tweets would you like to use for analysis (default:200)")
 #   if twtnum == "":
 #       twtnum = 200
 #   c = company(ticker,companyt,int(twtnum))        
 #   c.main()
c = company("INTC","Intel",200)
c.main()    