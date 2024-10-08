import tweepy
import os
from os.path import join, dirname
from dotenv import load_dotenv
import random
import time
from datetime import datetime, timedelta

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


# Autenticación
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = secret=os.getenv('ACCESS_TOKEN_SECRET')
bearer_token=os.getenv('BEARER_TOKEN')


def authentication():
    try:
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    except tweepy.TweepyException as e:
        print(f"Error de autenticación: {e}")

def publish(id):
    try:
        client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret) 
        api = authentication()
        image_path = f'./images/image({id}).png'
        media = api.media_upload(image_path)
        media_id = media.media_id_string
        client.create_tweet(text=f'image {id}/100',media_ids=[media_id])
       
    except tweepy.TweepyException as e:
        print(f"Error: {e}")
    finally:
        print("Se ha completado la tarea")

def main():
    while True:
        now = datetime.now() - timedelta(hours=0)
        if now.hour == 20 and now.minute == 9:
            publish(random.randint(0,100))
            publish(1)
            time.sleep(60)
        time.sleep(1)

def publish_test():
    try:
        client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret) 
        api = authentication()
        client.create_tweet(text=f'This is a tweer test')
    except tweepy.TweepyException as e:
        print(f"Error: {e}")
    finally:
        print("Se ha completado la tarea")
publish_test()