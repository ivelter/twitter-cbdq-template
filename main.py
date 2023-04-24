import dotenv
import tweepy
from os import listdir
from random import choice

def getrandomimg() -> str:
    return './img/' + choice(listdir('./img'))

consumerkey = dotenv.get_key("CONSUMER_KEY")
consumersecret = dotenv.get_key("CONSUMER_SECRET")
tokenkey = dotenv.get_key("TOKENKEY")
tokensecret = dotenv.get_key("TOKENSECRET")

auth = tweepy.OAuthHandler(consumer_key=consumerkey, consumer_secret=consumersecret)
auth.set_access_token(key=tokenkey, secret=tokensecret)
api = tweepy.API(auth)

ret = api.media_upload(getrandomimg())

api.update_status(media_ids=[ret.media_id_string], status="")