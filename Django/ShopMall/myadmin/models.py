from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    gender = models.IntegerField(default=1)
    address = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=11)
    email = models.CharField(max_length=30)
    state = models.IntegerField(default=1)
    # 需要留意 auto_now, auto_now_add的区别
    # http://blog.sina.com.cn/s/blog_9e2e84050101iltd.html
    update_time = models.DateTimeField(auto_created=True, auto_now=True)
    create_time = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.name