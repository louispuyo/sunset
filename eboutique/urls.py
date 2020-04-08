from django.conf.urls import url, re_path
from django.urls import path
from .views import *

urlpatterns = [
    url('boutique/', HomePage, name='boutique'),
    path('about/', aboutView, name='about'),
    path('contact/', contactView, name='contact'),
    path('home/', HomeView, name='home')
]
