from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time
 
analyzer = SentimentIntensityAnalyzer()
 
conn = sqlite3.connect('twitter.db')
c = conn.cursor()
 
def create_table():
  try:
    c.execute("CREATE TABLE IF NOT EXISTS sentimiento(unix REAL, tweet TEXT, sentimiento REAL)")
    c.execute("CREATE INDEX fast_unix ON sentimiento(unix)")
    c.execute("CREATE INDEX fast_tweet ON sentimiento(tweet)")
    c.execute("CREATE INDEX fast_sentiment ON sentimiento(sentimiento)")
    conn.commit()
  except Exception as e:
    print(str(e))
create_table()
 
#consumer key, consumer secret, access token, access secret.
ckey="VXJgjUC7sKWZiSB8bEKrtrUNF"
csecret="VF0SmSfHBJOG9Cq2vPE6fdqu3wEzo2pEwbBx1urewvDrbuMxAV"
atoken="1442979107499806721-ZLSu5ZJEdGqdqHmg6JXhbqMgEatXN3"
asecret="0xq2d38kxZ5ogm91R969zHnBrbijySuwpdy44cmY548SD"
 
class listener(StreamListener):
 
  def on_data(self, data):
    try:
      data = json.loads(data)
      tweet = unidecode(data['text'])
      time_ms = data['timestamp_ms']
      vs = analyzer.polarity_scores(tweet)
      sentimiento = vs['compound']
      print(time_ms, tweet, sentimiento)
      c.execute("INSERT INTO sentimiento (unix, tweet, sentimiento) VALUES (?, ?, ?)",
            (time_ms, tweet, sentimiento))
      conn.commit()
 
    except KeyError as e:
      print(str(e))
    return(True)
 
  def on_error(self, status):
    print(status)
 
while True:
 
  try:
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    analisis= twitterStream.filter(track=["macri"])
    print(analisis.head())
  except Exception as e:
    print(str(e))
    time.sleep(5)