from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<html><body>Hello, World!</html></body>')

def about(request):
    return HttpResponse("Here is the About page. Want to return home? <a href='/'>Back Home</a>")
