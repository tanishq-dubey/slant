import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    def __init__(self):
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Auth Error!")

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'netural'
        else:
            return 'negative'

    def get_tweets(self, query, start_date, end_date, count = 10):
        tweets = []
        page = 1
        try:
            while True:
                fetched_tweets = self.api.search(q = query, count = count, page = page)
                for tweet in fetched_tweets:
                    print(tweet.text)
                    if tweet.created_at < end_date and tweet.created_at > start_date:
                        parsed_tweet = {}
                        parsed_tweet['text'] = tweet.text
                        parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                        if tweet.retweet_count > 0:
                            if parsed_tweet not in tweets:
                                tweets.append(parsed_tweet)
                        else:
                            tweets.append(parsed_tweet)
                if len(tweets) >= count:
                    return tweets
                else:
                    page = page + 1
        except tweepy.TweepError as e:
            print("Error: " + str(e))

