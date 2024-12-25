from django.urls import path
from main.views import index, waage, biene, wildbiene, honig, impressum, kontakt

urlpatterns = [
    path('', index, name='index'),
    path('waage/', waage, name='waage'),
    path('biene/', biene, name='biene'),
    path('wildbiene/', wildbiene, name='wildbiene'),
    path('honig/', honig, name='honig'),
    path('kontakt/', kontakt, name='kontakt'),
    path('impressum/', impressum, name='impressum'),
]