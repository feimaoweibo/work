from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def teacher(req):
    return HttpResponse("这是teacher的一个视图")

def v2_exception(r):
    raise Http404
    return HttpResponse("OK")
