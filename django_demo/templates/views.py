import datetime

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sayHello(request):
    s="社会主义接班人"
    current_time=datetime.datetime.now()
    html="<html><head></head><body><h1> %s </h1><p> %s </p></body></html>"% (s,current_time)
    return HttpResponse(html)
def showUser(request):
    list=[{id:1,"name":"jack"},{id:2,"name":"rose"}]
    return render("users.html",{"users":list})