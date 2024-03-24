from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os
import plotly.graph_objs as go


load_dotenv()

API_KEY = os.getenv('API_KEY')
CHANNEL_ID_HORNER_MARSCH = os.getenv('CHANNEL_ID_HORNER_MARSCH')

def index(request):
    # GET Parameter from the html page 
    days = request.GET.get('days', '14')

    y1_min = request.GET.get('y1_min', None)
    y1_max = request.GET.get('y1_max', None)
    y2_min = request.GET.get('y2_min', None)
    y2_max = request.GET.get('y2_max', None)

    url = f'https://api.thingspeak.com/channels/{CHANNEL_ID_HORNER_MARSCH}/feeds.json?api_key={API_KEY}&round=2&days={days}&timescale=30'

    response=requests.get(url).json()

    feeds = response['feeds']
    

    # Initialize variables to store the last valid data points
    last_valid_field1 = None
    last_valid_field2 = None

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

    # for feed in feeds1:
    #     x_data.append(feed['created_at'])
    #     last_valid_field1 = float(feed['field1']) if feed['field1'] is not None else last_valid_field1
    #     field1_data.append(last_valid_field1)

    # # Extract data from the second API response
    # for feed in feeds2:
    #     last_valid_field2 = float(feed['field2']) if feed['field2'] is not None else last_valid_field2
    #     field2_data.append(last_valid_field2)

    # Create traces
    trace1 = go.Scatter(x=x_data, y=field1_data, mode='lines', name='Gewicht', yaxis='y')
    trace2 = go.Scatter(x=x_data, y=field2_data, mode='lines', name='Temperatur', yaxis='y2')

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
            ),
            range=[float(y1_min), float(y1_max)] if y1_min is not None and y1_max is not None and y1_min != '' and y1_max != '' else None
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
            side='right',
            range=[float(y2_min), float(y2_max)] if y2_min is not None and y2_max is not None and y2_min != '' and y2_max != '' else None
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