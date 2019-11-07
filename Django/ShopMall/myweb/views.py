from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myadmin.models import Types, Goods, Users
import time


# Create your views here.


def t(request):
    return HttpResponse("Hello world Myweb")
def t2(request):
    return render_to_response("./myweb/test.html")


# 公共信息加载函数
def loadinfo():
    context = {}
    context['type0list'] = Types.objects.filter(pid=0)
    return context

# 网站首页
def index(request):
    context = loadinfo()
    return render(request, "myweb/index.html", context)

# 商品列表页
def list(request):
    context = loadinfo()
    list = Goods.objects.filter()
    if request.GET.get('tid', '') != '':
        tid = str(request.GET.get('tid', ''))
        list = list.filter(typeid__in=Types.objects.only('id').filter(path__contains=',' + tid + ','))
    context['goodslist'] = list
    return render(request, "myweb/list.html", context)


# 商品详情页
def detail(request, gid):
    context = loadinfo()
    ob = Goods.objects.get(id=gid)
    ob.clicknum += 1
    ob.save()
    context['goods'] = ob
    return render(request, "myweb/detail.html", context)

# 会员登录表单
def login(request):
    return render(request, "myweb/login.html")
# 会员执行登录
def dologin(request):
    verifycode = request.session['verifycode']
    code = request.POST['code'].lower()
    if verifycode != code:
        context = {'info': "验证码错误"}
        return render(request, "myweb/login.html", context)
    try:
        # 根据帐号获取登录者信息
        user = Users.objects.get(username=request.POST['username'])
        # 判断当前用户是否是后台管理员用户
        if user.state == 0 or user.state == 1:
            # 验证密码
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'], encoding="utf8"))
            if user.password == m.hexdigest():
                # 此处登录成功，将当前登录信息放入到session中并跳转页面
                # print(json.dumps(user))
                request.session['user'] = user.dePosit()
                return redirect(reverse('index'))
            else:
                context = {'info': "登录密码错误"}
                return render(request, "myweb/login.html", context)
        else:
            context = {'info': "此用户为禁用用户"}
            return render(request, "myweb/login.html", context)
    except:
        context = {'info': "登录用户不存在！"}
        return render(request, "myweb/login.html", context)

# 用户退出
def logout(request):
    # 1、清除登录的session信息
    del request.session['user']
    # 2、跳转到登录页面
    return redirect(reverse('index'))
# 用户注册页面
def register(request):
    return render(request, "myweb/register.html")
# 用户注册页面的表单
def doregister(request):
    try:
        user = Users.objects.all()
        if user.filter(username=request.POST['username']):
            context = {'info': "此用户名已经注册"}
        else:
            ob = Users()
            ob.username = request.POST['username']
            ob.name = request.POST['name']
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'], encoding="utf8"))
            ob.password = m.hexdigest()
            if request.POST['password'] == request.POST['repassword']:
                ob.address = request.POST['address']
                ob.email = request.POST['email']
                ob.phone = request.POST['phone']
                ob.code = request.POST['code']
                ob.addtime = time.time()
                ob.save()
                return render(request, "myweb/login.html")
            else:
                context = {'info': "请重新输入密码"}
            return render(request, "myweb/register.html", context)
    except:
        context = {'info': "注册失败"}
    return render(request, "myweb/info.html", context)

