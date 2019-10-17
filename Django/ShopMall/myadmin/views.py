from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.


def t(request):
    return HttpResponse("Hello world Myadmin")

def t3(request):
    return render_to_response("./myadmin/test.html")