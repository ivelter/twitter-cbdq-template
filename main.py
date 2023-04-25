import dotenv
import tweepy
from os import listdir
from os import environ
from random import choice

def getrandomimg() -> str:
    return 'img/' + choice(listdir('./img'))

dotenv.load_dotenv(".env")
consumerkey = environ.get("CONSUMER_KEY")
consumersecret = environ.get("CONSUMER_SECRET")
tokenkey = environ.get("TOKENKEY")
tokensecret = environ.get("TOKENSECRET")

auth = tweepy.OAuthHandler(consumer_key=consumerkey, consumer_secret=consumersecret)
auth.set_access_token(key=tokenkey, secret=tokensecret)
api = tweepy.API(auth)

ret = api.media_upload(getrandomimg())

api.update_status(media_ids=[ret.media_id_string], status="")
# api.update_status(status="Hello world")