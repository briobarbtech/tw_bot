import tweepy
import os
from os.path import join, dirname
from dotenv import load_dotenv
import random
import time
from datetime import datetime, timedelta
from PIL import Image

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
dir= 'images/'

# Autenticación
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = secret=os.getenv('ACCESS_TOKEN_SECRET')
bearer_token=os.getenv('BEARER_TOKEN')

def loadImages(folder):
    images = {}
    for archivo in os.listdir(f"{dir}cap_{folder}"):
        if archivo.endswith(('jpg', 'png', 'jpeg')):
            img = Image.open(os.path.join(f"{dir}cap_{folder}", archivo))
            images[archivo] = img
    return images

def authentication():
    try:
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    except tweepy.TweepyException as e:
        print(f"Error de autenticación: {e}")

def publish(content):
    try:
        client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret) 
        api = authentication()
        image_path = content[0]
        media = api.media_upload(image_path)
        media_id = media.media_id_string
        client.create_tweet(text=f'image {id}/100 \n\n Link: {content[1]}',media_ids=[media_id])
       
    except tweepy.TweepyException as e:
        print(f"Error: {e}")
    finally:
        print("Se ha completado la tarea")
def lengthFolder(dir):
    folders = [nombre for nombre in os.listdir(dir) if os.path.isdir(os.path.join(dir, nombre))]
    length_folders = len(folders)
    return length_folders

def chooseContent():
    length_folder = lengthFolder(dir)
    choosed_folder = random.randint(1,length_folder)
    length_images = len(loadImages(choosed_folder))
    choosed_image = random.randint(1,length_images)
    images = f"{dir}cap_{choosed_folder}/image ({choosed_image})"
    link = f"https://www.webtoons.com/es/canvas/contrast-resistance/tren-y-resistencia/viewer?title_no=516436&episode_no={choosed_folder}"
    return [images,link]


def main():
    while True:
        now = datetime.now() - timedelta(hours=0)
        if now.hour == 20 and now.minute == 9:
            publish(chooseContent())
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
#publish_test()

