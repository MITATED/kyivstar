from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def test(request):
    name = "Орловский"
    b = Application.objects.filter(master__username=name, date="2018-01-23")
    x = ""
    for i in b:
        x += i.__str__() + "<br />"
    return HttpResponse(x)
