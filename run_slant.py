import slant_lib.slant

def main():
    slant_api = slant.TwitterClient()
    start_date = datetime.datetime(2017, 6, 1, 0, 0, 0)
    end_time = datetime.datetime(2017, 7, 1, 0, 0, 0)
    tweets = slant_api.get_tweets('AAPL', start_date, end_date, 50)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
