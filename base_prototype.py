from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "222364908-hzDxdW8S3kny95UoSpB8KWDsu5SXD7miXGzv5oU3"
access_token_secret = "KxxXLZkv6ioINuU3rFRdRDwZ4dWBF6snBaP3o8Hx4SjQj"
consumer_key = "1896uddb7q0H7wXl1Snpny3Hm"
consumer_key_secret ="YFtmhrtZQ9iptyBC7PWCkIjBRIUCjkrcxAdFIuTQxt0R9GW3es"


class mystreamlistener(StreamListener):
    
    def on_data(self,data):
        tweet = json.loads(data)
        print (tweet['text'])
        return True
        
    def on_error(self,status):
        print status



if __name__ == '__main__':
    streamdata = mystreamlistener()
    auth = OAuthHandler(consumer_key,consumer_key_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth,streamdata)
    
    stream.filter(track=['flood','chennai','cuddalore'])