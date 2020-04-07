from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app01 import models
from app01 import serializers
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from app01.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
# Create your views here.

# 列出所有的出版社或者创建一个新的出版社操作

'''
class PublisherList(generics.ListCreateAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer # 使用具体序列化类的名字
    # 权限设置，未元组格式内容。如果值为空，则所有人都能查看；permissions.IsAuthenticatedOrReadOnly表示登陆者均可以修改；
    # IsOwnerOrReadOnly表示只有录入者才能修改自己录入的内容
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    # 为登陆用户创建可以POST创建数据的权利
    def perform_create(self, serializer):
        serializer.save(operator=self.request.user)
'''

'''
# 具体到一个出版社的数据，进行查看、修改、删除操作
class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer # 使用具体序列化类的名字
    # 权限设置，未元组格式内容。如果值为空，则所有人都能查看；permissions.IsAuthenticatedOrReadOnly表示登陆者均可以修改；
    # IsOwnerOrReadOnly表示只有录入者才能修改自己录入的内容
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
'''
# 使用viewsets方式，对出版社进行各种操作
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    '''
    权限设置，未元组格式内容。如果值为空，则所有人都能查看；permissions.IsAuthenticatedOrReadOnly表示登陆者均可以修改；
    IsOwnerOrReadOnly表示只有录入者才能修改自己录入的内容
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    # 为登陆用户创建可以POST创建数据的权利
    def perform_create(self, serializer):
        serializer.save(operator=self.request.user)
'''
# 列出所有书或者添加一本新书的操作
class BookList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer # 使用具体序列化的类
    # 权限认证
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
# 具体一本书的数据，进行查看，修改，删除操作
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer # 使用具体序列化的类
    # 权限认证
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
'''
# 使用视图集viewsets方式，对图书进行各种操作
class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer # 使用具体序列化的类
    # 权限认证
    perimission_classes = (permissions.IsAuthenticatedOrReadOnly, )

