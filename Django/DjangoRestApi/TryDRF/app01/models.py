from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name="名称", unique=True)
    address = models.CharField(max_length=128, verbose_name="地址")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

'''
传入数据操作实例
>>> from app01 import models
>>> p1 = models.Publisher(name="番茄出版社", address="番茄街")
>>> p1
<Publisher: 番茄出版社>
>>> p1.save()
'''