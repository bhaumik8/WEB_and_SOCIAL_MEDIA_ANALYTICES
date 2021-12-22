import tweepy
import sys
import os
import codecs

f = codecs.open('name.txt', 'a', encoding='utf-8')

CONSUMER_KEY = "***"
CONSUMER_SECRET = "***"
ACCESS_TOKEN = "***"
ACCESS_TOKEN_SECRET = "***"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


class BasicTwitterListener(tweepy.StreamListener):
    def set_up(self):
        self.start_tweet = 0

    def on_status(self, status):
        try:
            new_tweet = status.text.replace('\n', ' ')
            if len(new_tweet)< 5:
              return True
            f.write(new_tweet + "\n")
            self.start_tweet += 1
            print(self.start_tweet)
                
            if self.start_tweet == 1000:
                f.close()
                return False

        except Exception as e:
            print('exception when reading from stream:')
            pass

    def on_error(self, status_code):
        print('Encounter error with status code:' + str(status_code) )
        return True

    def on_timeout(self):
        print('Timeout')
        return True


l = BasicTwitterListener()
l.set_up()

live_stream = tweepy.streaming.Stream(auth, l)
keywords = ['trump']
live_stream.filter(track=keywords, languages = ['en'], follow=None)


#Historical data, after the access_token secret same as above

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

f2 = open('filename.txt', 'a')
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search,
                           q = 'brand',
                           until = '2021-05-02',
                           truncated = False,
                           lang = 'en',
                           tweet_mode='extended').items():
    if 'retweeted_status' in tweet._json:
 		    new_tweet = tweet._json['retweeted_status']['full_text'].replace('\n', ' ')
    else:
 		    new_tweet = tweet._json['full_text'].replace('\n', ' ')
    f2.write(str(tweet.created_at) + '***' + new_tweet + "\n")
    #f2.write('This is a test' + '\n')
    print(str(tweet.created_at) + '***' + new_tweet)
    
f2.close()
































