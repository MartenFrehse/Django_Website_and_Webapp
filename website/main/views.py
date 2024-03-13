from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'active_link': 'index'})

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