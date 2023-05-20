from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def mahi(request):
    return HttpResponse('<marquee>hi ra how are you</marquee>')

def ram(request):
    return HttpResponse('<marquee><h1>hii ra how r you my name is mahesh iam from kurnool</h1></marquee>')
