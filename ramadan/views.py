import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) :
    now = datetime.datetime.now()
    return render(request, "ramadan/index.html", {
        "ramadan": now.month == 3 and now.day == 11
    })
