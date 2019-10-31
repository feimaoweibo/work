from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    gender = models.IntegerField(default=1)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=30)
    state = models.IntegerField(default=1)
    # 需要留意 auto_now, auto_now_add的区别
    # http://blog.sina.com.cn/s/blog_9e2e84050101iltd.html
    update_time = models.DateTimeField(auto_created=True, auto_now=True)
    create_time = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.name

# 创建类型
class Types(models.Model):
    name = models.CharField(max_length=30)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# 商品信息数据表
class Goods(models.Model):
    typeid = models.IntegerField()
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    descr = models.TextField()
    price = models.FloatField()
    picname = models.CharField(max_length=255)
    state = models.IntegerField(default=1)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.IntegerField()

    def __str__(self):
        return self.goods

# 订单信息数据表
class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.IntegerField()
    total = models.FloatField()
    status = models.IntegerField()

    def __str__(self):
        return self.linkman

# 商品详情页
class Detail(models.Model):
    ordersid = models.IntegerField()
    goodsid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.FloatField()
    num = models.IntegerField()

    def __str__(self):
        return self.name



