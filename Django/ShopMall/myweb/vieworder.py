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
