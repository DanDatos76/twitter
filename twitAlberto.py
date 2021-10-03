from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time
 
analyzer = SentimentIntensityAnalyzer()
 
#consumer key, consumer secret, access token, access secret.
ckey="F2pIrutjymGr9vZuqTeViAymw"
csecret="QFLTXwFJZNuR6i00IswAZIgaKsKl5AtmPufoSaRnR57ER2yVxS"
atoken="879408865997201408-QJDeVNKYBsTdp97caK0qFV454YYwRLp"
asecret="gLNfeVRjT7LrDaWWSgCX0ZRu6TeTPBquTxlYKQ4hUzAka"
 
conn = sqlite3.connect('twitter-Alberto.db')
c = conn.cursor()
 
def create_table():
  try:
    c.execute("CREATE TABLE IF NOT EXISTS sentimiento(unix REAL, tweet TEXT, sentimiento REAL)")
    c.execute("CREATE INDEX fast_unix ON sentimiento(unix)")
    c.execute("CREATE INDEX fast_tweet ON sentimiento(tweet)")
    c.execute("CREATE INDEX fast_sentimiento ON sentimiento(sentimiento)")
    conn.commit()
  except Exception as e:
    print(str(e))
create_table()
 
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
    twitterStream.filter(track=["alberto fernandez"])
  except Exception as e:
    print(str(e))
    time.sleep(5)


alberso= pd.read_db('twitter-Alberto.db')

#CSV A DICCIONARIO DE PYTHON
alberso.to_dict('records')
alberso.head()


