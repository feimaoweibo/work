from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myadmin.models import Types
from PIL import Image
import time, os, json

# 浏览商品类别信息
def typeindex(request):
    '''
    执行数据查询，并放置到模版中
    :param request: concat负责把path和id拼接成一个内容。
           说明文档查询：https://docs.djangoproject.com/en/1.11/ref/models/querysets/#extra
    :return: 如果是mysql版本，需要时hi用concat，如果是sqlite，则需要使用 || 链接path和id
             list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    '''
    list = Types.objects.extra(select = {'_has': 'path || id'}).order_by('_has')
    # 遍历查询结果，为每个结果对象追加一个pname属性，目的用于缩进标题
    for ob in list:
        ob.pname = '...'*(ob.path.count(',')-1)
    context = {"typeslist":list}
    return render(request, "myadmin/type/index.html", context)
# 商品类别信息添加表单
def typeadd(request,tid):
    # 获取父类别信息，若没有则默认为根类别信息
    if tid == '0':
        context = {'pid': 0, 'path': '0', 'name': '根类别'}
    else:
        ob = Types.objects.get(id=tid)
        context = {'pid': ob.id, 'path': ob.path+str(ob.id)+',', 'name': ob.name}
    return render(request, "myadmin/type/add.html", context)

# 执行商品类别信息添加
def typeinsert(request):
    try:
        ob = Types()
        ob.name = request.POST['name']
        ob.pid = request.POST['pid']
        ob.path = request.POST['path']
        ob.save()
        context = {'info': "添加成功！"}
    except:
        context = {'info': "添加失败！！！"}
    return render(request, "myadmin/info.html", context)
