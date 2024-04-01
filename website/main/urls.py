from django.urls import path
from main.views import index, biene, wildbiene, honig, impressum, kontakt

urlpatterns = [
    path('', index, name='index'),
    path('biene/', biene, name='biene'),
    path('wildbiene/', wildbiene, name='wildbiene'),
    path('honig/', shop, name='honig'),
    path('kontakt/', kontakt, name='kontakt'),
    path('impressum/', impressum, name='impressum'),
]