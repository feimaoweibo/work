from django.db import models
import time
# Create your models here.

class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)

    # 一对一关系
    room = models.OneToOneField("ClassRoom")

    # 将方法作为列名称显示，必须要有返回值
    def curTime(self):
        return time.time()
    # 将列名称设置为短字段（如为中文），使用func.short_description = “短字段”
    curTime.short_description = "当前时间"
    # 同时该方法排序，使用func.admin_order_field = "依据"
    curTime.admin_order_field = "name"

    # 关联对象,使用方法
    def getRoomName(self):
        return self.room.name
    getRoomName.short_description = "上课教室"



    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    # 一对多关系
    room = models.ForeignKey("ClassRoom")

    def __str__(self):
        return self.name
