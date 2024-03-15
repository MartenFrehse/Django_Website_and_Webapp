from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
CHANNEL_ID_HORNER_MARSCH = os.getenv('CHANNEL_ID_HORNER_MARSCH')


def index(request):
    url = f'https://api.thingspeak.com/channels/{CHANNEL_ID_HORNER_MARSCH}/feeds.json?api_key={API_KEY}'
    response=requests.get(url).json()
    print(response)

    channel_info = response['channel']
    feeds = response['feeds']

    return render(request, 'main/index.html', {'active_link': 'index', 'channel_info': channel_info, 'feeds': feeds})

def biene(request):
    return render(request, 'main/biene.html', {'active_link': 'biene'})

def impressum(request):
    return render(request, 'main/impressum.html')

def kontakt(request):
    return render(request, 'main/kontakt.html')

def shop(request):
    return render(request, 'main/shop.html', {'active_link': 'shop'})

def wildbiene(request):
    return render(request, 'main/wildbiene.html', {'active_link': 'wildbiene'})