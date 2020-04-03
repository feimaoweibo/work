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
class PublisherList(APIView):
    # 列出所有的出版社或者创建一个新的出版社操作
    def get(self, request, format=None):
        queryset = models.Publisher.objects.all() # 查询出所有的出版社
        s = serializers.PublisherSerializer(queryset, many=True)
        return Response(s.data)
    def post(self, request, format=None):
        s = serializers.PublisherSerializer(data=request.data)
        if s.is_valid(): # 如果传入数据没问题
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST) #数据有问题则返回errors
'''
'''
class PublisherList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
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


# 具体到一个出版社的数据，进行查看、修改、删除操作
'''
class PublisherDetail(APIView):
    def get_object(self, pk): #通过输入的主键，先查询存在具体的出版社与否
        try:
            return models.Publisher.objects.get(pk=pk)
        except models.Publisher.DoesNotExist:
            raise Http404
    # 查看具体的出版社信息
    def get(self, request, pk, format=None):
        publisher = self.get_object(pk)
        s = serializers.PublisherSerializer(publisher)
        return Response(s.data)
    # 修改出版社信息
    def put(self, request, pk, format=None):
        publisher = self.get_object(pk)
        s = serializers.PublisherSerializer(publisher, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    # 删除出版社信息
    def delete(self, request, pk, format=None):
        publisher = self.get_object(pk)
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''
class PublisherDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''
class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer # 使用具体序列化类的名字
    # 权限设置，未元组格式内容。如果值为空，则所有人都能查看；permissions.IsAuthenticatedOrReadOnly表示登陆者均可以修改；
    # IsOwnerOrReadOnly表示只有录入者才能修改自己录入的内容
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

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


# 创建根视图模式，进入API后就行导流模式
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'publishers': reverse('publisher-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format)
    })
