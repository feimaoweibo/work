from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

# Create your views here.
from myadmin.models import Users

def t(request):
    return HttpResponse("Hello world Myadmin")

def t3(request):
    return render_to_response("./myadmin/test.html")
# 执行分页操作
def users(request, pIndex=1):
    # 获取会员信息
    list = Users.objects.filter()
    # 判断并封装搜索条件
    # 定义一个用于维持搜索条件的变量
    where = []
    if request.GET.get('name', '') != '':
        list = list.filter(name__contains=request.GET.get('name'))
        where.append('name=' + request.GET.get('name'))
    if request.GET.get('sex', '') != '':
        list = list.filter(sex=request.GET['sex'])
        where.append('sex=' + request.GET.get('sex'))
    # 传入数据和页大小来创建分页对象
    p = Paginator(list, 4)
    # 判断页号没有值时初始化为1
    if pIndex == '':
        pIndex == '1'
    pIndex = int(pIndex) # 类型转换int
    list2 = p.page(pIndex)# 获取当前页数据
    plist = p.page_range #获取页码信息

    # 封装分页信息
    context = {'userslist':list2, 'plist':plist, 'pIndex':pIndex, 'where':where}
    return render(request, 'myadmin/users/index.html', context)

# 后台首页
def index(request):
    return render(request, 'myadmin/index.html')

# =====================后台会员管理===================
# 浏览会员
def usersindex(request):
    # 执行数据查询，并放置到模版中
    list = Users.objects.all()
    context = {"userslist":list}
    return render(request, 'myadmin/users/index.html', context)
# 会员信息添加表单
def usersadd(request):
    return render(request, 'myadmin/users/add.html')
# 执行会员信息添加
def usersinsert(request):
    try:
        # 步骤1、创建用户；2、保存用户
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        # 获取密码，并使用MD5方式加密密码
        import hashlib
        m = hashlib.md5()
        # update()函数要求参数是bytes
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()

        ob.gender = request.POST['sex']
        ob.address = request.POST['address']
        ob.state = 1
        ob.save()
        context = {'info': '添加成功！'}
    except:
        context = {'info': '添加失败'}
    return render(request, "myadmin/info.html", context)
