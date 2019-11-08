from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myadmin.models import Types, Goods, Users, Orders, Detail
import time

# 公共信息加载函数
def loadinfo():
    context = {}
    context['type0list'] = Types.objects.filter(pid=0)
    return context

# 个人中心
def personal(request):
    '''
    读取当前用户信息后用此信息渲染页面，供用户修改
    注意：这个资料不应该包含密码信息
    :param request:
    :return:
    '''
    user = Users.objects.get(username=request.session['user']['username'])
    context = {'users': user}
    return render(request, "myweb/personal.html", context)

# 打开会员编辑
def peredit(request):
    try:
        ob = Users.objects.get(username=request.session['user']['username'])
        context = {'user': ob}
        return render(request, "myweb/peredit.html", context)
    except:
        context = {'info': "没有找到要修改的信息"}
    return render(request, "myweb/info.html", context)

# 执行会员的编辑操作
def perupdate(request):
    try:
        ob = Users.objects.get(username=request.session['user']['username'])
        ob.name = request.POST['name']
        ob.address = request.POST['address']
        ob.username = request.POST['username']
        ob.code = request.POST['code']
        ob.sex = request.POST['sex']
        ob.email = request.POST[email]
        ob.save()
        context = {'info': "修改个人资料成功"}
    except:
        context = {'info': "修改个人资料失败！"}
    return render(request, "myweb/info.html", context)

# 购物车
def shopcart(request):
    context = loadinfo()
    if 'shoplist' not in request.session:
        request.session['shoplist'] = {}
    return render(request, "myweb/shopcart.html", context)


