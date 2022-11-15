import tweepy, config
from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods = ['POST'])
def search():
    search = ""
    sentimentList = []
    if request.method == 'POST':
        search = request.form.get("Topic")
        consumer_key = config.api_key
        consumer_secret = config.api_secret
        access_token = config.access_token
        access_secret = config.token_secret

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)

        public_tweets = api.search_tweets(search)

        for tweet in public_tweets:
            print(tweet.text)
            analysis = TextBlob(tweet.text)
            sentimentList.append(analysis.sentiment)
            print(sentimentList)
            # print(analysis.sentiment)
            return tweet.text

    # consumer_key = config.api_key
    # consumer_secret = config.api_secret
    # access_token = config.access_token
    # access_secret = config.token_secret

    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # auth.set_access_token(access_token, access_secret)

    # api = tweepy.API(auth)

    # public_tweets = api.search_tweets(search)
    # print(public_tweets)

    # for tweet in public_tweets:
    #     print(tweet.text)
    #     analysis = TextBlob(tweet.text)
    #     print(analysis.sentiment)

    # return render_template('index.html')

# consumer_key = config.api_key
# consumer_secret = config.api_secret
# access_token = config.access_token
# access_secret = config.token_secret

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# auth.set_access_token(access_token, access_secret)

# api = tweepy.API(auth)

# public_tweets = api.search_tweets(search)
# print(public_tweets)

# for tweet in public_tweets:
#     print(tweet.text)
#     analysis = TextBlob(tweet.text)
#     print(analysis.sentiment)

if __name__ == '__main__':
    app.run(debug=True)