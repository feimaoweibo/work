from rest_framework import serializers
from app01 import models
'''
#方法一：手动填写序列化
class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # ID自增
    name = serializers.CharField(max_length=32)
    address = serializers.CharField(max_length=128)
    # 创建数据方法，并检验相关健的值是否为空
    def create(self, validated_data):
        return models.Publisher.objects.create(**validated_data)
    # 更新数据方法
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.save()
        return instance
'''
# 方法二 继承ModelSerializer类
class PublisherSerializer(serializers.ModelSerializer):
    # 重写operator字段，反向查找出用户名
    operator = serializers.ReadOnlyField(source="operator.username")

    class Meta:
        model = models.Publisher
        fields = (
            "id",
            "name",
            "address",
            "operator"
        )

class BookSerializer(serializers.HyperlinkedModelSerializer): # HyperlinkedModelsSerializer超链接
    # 重写publiser字段，反向查找出publisher名字
    #publisher = serializers.StringRelatedField(source="publisher.name")

    class Meta:
        model = models.Book
        fields = (
            "id",
            "title",
            "publisher"
        )

    '''
    操作实例-----查询
    >>> from app01 import models, serializers
    >>> p1 = models.Publisher.objects.first()
    >>> p1
    <Publisher: 番茄出版社>
    >>> serializer = serializers.PublisherSerializer(p1)
    >>> serializer.data
    {'id': 1, 'name': '番茄出版社', 'address': '番茄街'}
    操作实例-----新增
    >>> from app01 import models, serializers
    >>> p3 = {"name":"柑橘出版社", "address":"柑橘街"}
    >>> serializer = serializers.PublisherSerializer(data=p3)
    >>> serializer.is_valid()
    True
    >>> serializer.validated_data
    OrderedDict([('name', '柑橘出版社'), ('address', '柑橘街')])
    >>> serializer.save()
    <Publisher: 柑橘出版社>

    '''