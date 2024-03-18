from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os
import plotly.graph_objs as go


load_dotenv()

API_KEY = os.getenv('API_KEY')
CHANNEL_ID_HORNER_MARSCH = os.getenv('CHANNEL_ID_HORNER_MARSCH')

def index(request):
    url = f'https://api.thingspeak.com/channels/{CHANNEL_ID_HORNER_MARSCH}/feeds.json?api_key={API_KEY}&round=2&days=14&timescale=30'
    response=requests.get(url).json()

    feeds = response['feeds']

    # Initialize variables to store the last valid data points
    last_valid_field1 = None
    last_valid_field2 = None

    # Extracting data for plotting
    # x_data = [feed['created_at'] for feed in feeds]
    # field1_data = [float(feed['field1']) for feed in feeds]
    # field2_data = [float(feed['field2']) for feed in feeds]
    x_data = []
    field1_data = []
    field2_data = []

    for feed in feeds:
        # Append the x_data
        x_data.append(feed['created_at'])

        # Process field1_data
        if feed['field1'] is not None:
            last_valid_field1 = float(feed['field1'])
        field1_data.append(last_valid_field1)

        # Process field2_data
        if feed['field2'] is not None:
            last_valid_field2 = float(feed['field2'])
        field2_data.append(last_valid_field2)

    # Create traces
    trace1 = go.Scatter(x=x_data, y=field1_data, mode='lines', name='Field 1', yaxis='y')
    trace2 = go.Scatter(x=x_data, y=field2_data, mode='lines', name='Field 2', yaxis='y2')

    # Define layout with multiple y-axes
    layout = go.Layout(
        title='Horner Marsch',
        yaxis=dict(
            title='Gewicht',
            titlefont=dict(
                color='blue'
            ),
            tickfont=dict(
                color='blue'
            )
        ),
        yaxis2=dict(
            title='Außentemperatur',
            titlefont=dict(
                color='red'
            ),
            tickfont=dict(
                color='red'
            ),
            overlaying='y',
            side='right'
        )
    )

    # Create figure
    fig = go.Figure(data=[trace1, trace2], layout=layout)

    # Convert the Plotly figure to JSON
    graph_json = fig.to_json()

    return render(request, 'main/index.html', {'active_link': 'index', 'graph_json': graph_json})

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