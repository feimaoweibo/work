from django.contrib import admin
from myadmin.models import Student, Teacher, ClassRoom
# Register your models here.

# 修改django默认站点名称、宣传语
admin.site.site_header = "欢迎来到django课程"
admin.site.site_title = "北京图灵学院"
admin.site.index_title = "学会Python走遍天下"

# 设置管理类，使用ModelAdmin方法
class ClassRoomAdmin(admin.ModelAdmin):
    pass
class TeacherAdmin(admin.ModelAdmin):
    # 修改页面显示数量（每页显示2个教师）
    list_per_page = 2
    # 选项操作修改位置
    actions_on_bottom = True
    actions_on_top = False# 默认在顶部
    # 控制列表中显示内容
    list_display = ['name', 'room', 'curTime', 'getRoomName']
    # 添加搜索框
    search_fields = ['name']
    # 分组
    fieldsets = (
        ("基本信息", {"fields": ["name"]}),
        ("课程信息", {"fields": ["room", "course"]}),
    )
# 设置管理类，使用装饰器方法
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass



admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Teacher, TeacherAdmin)
#admin.site.register(Student, StudentAdmin)