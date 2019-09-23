from django.shortcuts import render
from django.http import HttpResponse

from django.core.urlresolvers import reverse
# Create your views here.


def do_normalmap(request):
    return HttpResponse("This is normalmap")

def withparam(request, year, month):
    return HttpResponse("This is with param {0},{1}".format(year, month))

def do_app(r):
    return HttpResponse("这是个子路由")

def do_param2(r, pn):
    return HttpResponse("Page number is {0}".format(pn))

def extremParam(r, name):
    return HttpResponse("My name is {0}".format(name))

def revParse(r):
    return HttpResponse("Your requested URL is {0}".format(reverse("askname")))