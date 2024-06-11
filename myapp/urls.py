from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('subscribe/', subscriber, name='subscribe'),
    path('add_blog/', add_blog, name='add_blog')
]