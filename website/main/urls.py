from django.urls import path
from main.views import index, biene, wildbiene, honig, impressum, kontakt, waage

urlpatterns = [
    path('', index, name='index'),
    path('biene/', biene, name='biene'),
    path('wildbiene/', wildbiene, name='wildbiene'),
    path('honig/', honig, name='honig'),
    path('kontakt/', kontakt, name='kontakt'),
    path('impressum/', impressum, name='impressum'),
    path('waage/', waage, name='waage'),
]