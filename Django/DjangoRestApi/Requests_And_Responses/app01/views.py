from django.shortcuts import render
from app01 import models
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app01 import serializers

# Create your views here.

@api_view(['GET', 'POST']) #通过GET（查询）、POST(创建)
def publisher_list(request, format=None):
    '''
    列出所有的出版社，或者创建一个新的出版社
    '''
    if request.method == "GET":
        queryset = models.Publisher.objects.all() # 把所有出版社的数据赋值给queryset
        s = serializers.PublisherSerializer(queryset, many=True)
        return Response(s.data)
    if request.method == "POST":
        # 创建出版社
        s = serializers.PublisherSerializer(data=request.data)
        if s.is_valid(): #验证提交的数据真实性
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE']) # 对具体一个实例的数据进行GET(查询)、PUT(更改)、DELETE(删除)
def publisher_detail(request, pk, format=None): # pk为主键的ID
    try:
        publisher = models.Publisher.objects.get(pk=pk)
    except models.Publisher.DoesNotExist: #假如传递需要被查询的数据不存在，则返回404提示
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        s = serializers.PublisherSerializer(publisher)
        return Response(s.data)
    if request.method == 'PUT':
        s = serializers.PublisherSerializer(publisher, data=request.data)
        if s.is_valid(): #验证提交的数据真实性
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)