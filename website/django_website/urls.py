"""
URL configuration for django_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views


# from upload.views import image_upload
# from main.views import index, biene, wildbiene, shop, kontakt, impressum

urlpatterns = [
    path('', include('main.urls')),
    path('', include('todo.urls')), 
    # path('', index, name='index'),
    # path("", image_upload, name="upload"),
    # path('biene/', biene, name='biene'),
    # path('wildbiene/', wildbiene, name='wildbiene'),
    # path('shop/', shop, name='shop'),
    # path('kontakt/', kontakt, name='kontakt'),
    # path('impressum/', impressum, name='impressum'),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
