from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def one(request):
    return render(request, r"one.html")

def two(request):
    ct = dict()
    ct['name'] = "王小静"
    ct["name2"] = "李晓静"
    ct["name3"] = "张小静"
    return render(request, r'two.html', context=ct)

def three(request):
    ct = dict()
    ct["score"] = [88, 99, 45, 67, 89, 32]
    return  render(request, r'three.html', context=ct)

def four(request):
    ct = dict()
    ct["name"] = "李晓静"
    return render(request, r"four.html", context=ct)

def five_get(request):
    return render(request, r'five_get.html')

def five_post(request):
    print(request.POST)
    return render(request, r'one.html')

