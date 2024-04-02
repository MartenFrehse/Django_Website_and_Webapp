from background_task import background
import requests
from django.utils import timezone
from .models import API_Daten
import os

API_KEY = os.getenv('API_KEY')
CHANNEL_ID_HORNER_MARSCH = os.getenv('CHANNEL_ID_HORNER_MARSCH')

@background(schedule=600)  # Schedule the task to run every 10 minutes (600 seconds)
def fetch_and_store_data_from_thingspeak():
    api_url = f'https://api.thingspeak.com/channels/{CHANNEL_ID_HORNER_MARSCH}/feeds.json?api_key={API_KEY}&round=2&timescale=10'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        feeds = data['feeds']
        
        for feed in feeds:
            gewicht = float(feed['field1'])
            temperatur = float(feed['field2'])
            datum_zeit = timezone.now()

            # Save the data to the database
            API_Daten.objects.create(
                datum=datum_zeit.date(),
                zeit=datum_zeit.time(), 
                gewicht=gewicht,
                temperatur=temperatur,
                notiz="",
            )
    else:
        print("Error fetching data from Thingspeak:", response.status_code)