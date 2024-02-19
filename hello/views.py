from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request, "hello/index.html")

def lina(request):
    return HttpResponse("Hello, lina!")

def sara(request):
    return HttpResponse("Hello, sara")

def greet(request, name):
    return render(request, "hello/.greet.html", {
        "name": name.capitalize()
    })