from django.db import models

# Create your models here.
# 起名比较重要,不要跟系统重复
class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    gender = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    # 需要留意 auto_now, auto_now_add的区别
    # http://blog.sina.com.cn/s/blog_9e2e84050101iltd.html
    update_time = models.DateTimeField(auto_created=True, auto_now=True)
    create_time = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        db_table = "tlxy_users"  # 更改表名
		
class Types(models.Model):
	name = models.CharField(max_length=32)
	pid = models.IntegerField(default=0)
	path = models.CharField(max_length=255)

	class Meta:
		db_table = "type"


#商品信息数据表

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

	class Meta:
		db_table="goods"

	def dePosit(self):
		return{'id':self.id,'goods':self.goods,'picname':self.picname,'price':self.price,'descr':self.descr,'store':self.store,'m':1}

class Orders(models.Model):
	uid = models.IntegerField()
	linkman = models.CharField(max_length=32)
	address = models.CharField(max_length=255)
	code = models.CharField(max_length=6)
	phone = models.CharField(max_length=16)
	addtime = models.IntegerField()
	total = models.FloatField()
	status = models.IntegerField()

	class Meta:
		db_table="orders"


class Detail(models.Model):
	orderid = models.IntegerField()
	goodsid = models.IntegerField()
	name = models.CharField(max_length=32)
	price = models.FloatField()
	num = models.IntegerField()

	class Meta:
		db_table="detail"

