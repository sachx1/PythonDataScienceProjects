import tweepy
from textblob import TextBlob

consumer_key = 'PTO3c8rxWw7WhN3EKt0pM8VzH'
consumer_secret = '496dLVPVOpGmPh7pLAKG4pGf7R2yHZPTFMZn2Zjt6DPFSbjqG5'
access_token = '1096434375883919367-Mzo5ox0bJellGNqqE7FmSvT6sGfUAf'
access_secret = 'EJSb9oMb4x35Et75klLIflo2n9H30RwRZTthMD6LuUKNh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)