
# Create your views here.
from django.shortcuts import render
from .models import watch, collection
# Create your views here.


def contactView(request):

    return render(request, 'index.html')


def HomePage(request):
    content = {
        'collections': collection.objects.all()
    }
    return render(request, 'homepage.htm', content)


def aboutView(request):
    return render(request, 'about.htm')


def HomeView(request):
    return render(request, 'home.htm')
