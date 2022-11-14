import tweepy, config
from textblob import TextBlob

consumer_key = config.api_key
consumer_secret = config.api_secret
access_token = config.access_token
access_secret = config.token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)