import tweepy
import sqlite3
from tweepy import Stream
from tweepy import OAuthHandler
import streamlit as st
import pandas as pd
import numpy as np
import csv 
#from pymongo import MongoClient
import PIL
import os 
#from app import app, mongo
#from bson.json_util import dumps
#from bson.objectid import ObjectId
from flask import jsonify, request
import msvcrt
import  wget
import time
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import credentials



analyzer = SentimentIntensityAnalyzer()


consumer_key = "VXJgjUC7sKWZiSB8bEKrtrUNF"
consumer_secret ="VF0SmSfHBJOG9Cq2vPE6fdqu3wEzo2pEwbBx1urewvDrbuMxAV"
access_token ="1442979107499806721-ZLSu5ZJEdGqdqHmg6JXhbqMgEatXN3"
access_token_secret ="0xq2d38kxZ5ogm91R969zHnBrbijySuwpdy44cmY548SD"
printer2 =(
  consumer_key, consumer_secret,
  access_token, access_token_secret
)


class MyStreamListener(tweepy.Stream):
  def on_status(self, status):
    if hasattr(status, "retweeted_status"):  # Check if Retweet
        try:
            print(status.retweeted_status.extended_tweet["full_text"])

            f = open('./prueba1.json', 'w', encoding='utf-8')
            f.write(str([status.text]) + '\n')
            f.close
            
            
        except AttributeError:
            print(status.retweeted_status.text)
    else:
        try:
            print(status.extended_tweet["full_text"])
        except AttributeError:
            print(status.text)
         

printer2 =  MyStreamListener(
  consumer_key, consumer_secret,
  access_token, access_token_secret
)

# Filter realtime Tweets by keyword
#printer.filter(track=["mono"])
result= printer2.filter(track=["Messi"])
data =result


             
for tweet in result:
	 
  f = open('./prueba1.json', 'w', encoding='utf-8')
  f.write(str([result.text]) + '\n')
  f.close






 

