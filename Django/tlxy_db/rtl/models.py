from django.db import models

# Create your models here.

class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)

    def __str__(self):
        return self.school_name

class Manager(models.Model):
    manager_id = models.IntegerField()
    manager_name = models.CharField(max_length=20)
    # 一对一关系表
    my_school = models.OneToOneField(School)

    def __str__(self):
        return self.manager_name
class Teachers(models.Model):
    teachers_name = models.CharField(max_length=20)
    my_schools = models.ForeignKey("School")

    def __str__(self):
        return self.teachers_name

class Students(models.Model):
    students_name = models.CharField(max_length=20)
    teachers = models.ManyToManyField("Teachers")

    def __str__(self):
        return self.students_name
