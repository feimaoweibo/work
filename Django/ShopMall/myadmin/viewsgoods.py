from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myadmin.models import Types, Goods
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
    list = Types.objects.extra(select={'_has': 'path || id'}).order_by('_has')
    # 遍历查询结果，为每个结果对象追加一个pname属性，目的用于缩进标题
    for ob in list:
        ob.pname = '...'*(ob.path.count(',')-1)
        # print(list[0].__dict__)
    context = {"typeslist": list}
    return render(request, "myadmin/type/index.html", context)
# 商品类别信息添加表单
def typeadd(request,tid):
    # 获取父类别信息，若没有则默认为根类别信息
    if tid == '0':
        context = {'pid': 0, 'path': '0,', 'name': '根类别'}
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

# 商品类别信息删除表单
def typedel(request,tid):
    try:
        # 获取删除商品的子列表信息里，诺有数据，就禁止删除当前类别
        row = Types.objects.filter(pid=tid).count()
        if row > 0:
            context = {'info':'禁止删除：此类别下还有子类'}
            return render(request, "myadmin/info.html", context)
        ob = Types.objects.get(id=tid)
        ob.delete()
        context = {'info': '删除成功'}
    except:
        context = {'info': '删除失败'}
    return render(request, "myadmin/info.html", context)

# 商品类型信息编辑表单
def typeedit(request,tid):
    try:
        ob = Types.objects.get(id=tid)
        context = {'type': ob}
        return render(request, "myadmin/type/edit.html", context)
    except:
        context = {'info': '没有找到要修改的信息'}
    return render(request, "myadmin/info.html", context)

# 商品类型添加表单
def typeupdate(request,tid):
    try:
        ob = Types.objects.get(id=tid)
        ob.name = request.POST['name']
        ob.save()
        context = {'info': '修改成功'}
    except:
        context = {'info': '修改失败'}
    return render(request, "myadmin/info.html", context)

# ------------------后台商品信息管理------------------------
# 商品信息的页面
def goodsindex(request, pIndex=1):
    # 执行数据查询，并放置到模版中
    list = Goods.objects.all()
    for ob in list:
        ty = Types.objects.get(id=ob.typeid)
        ob.typename = ty.name # 判断并封装搜索条件
    # 传入数据和页大小来创建分页对象
    p = Paginator(list, 4)
    # 判断页号码没有值时，初始化为1
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex) # 类型转换int
    list2 = p.page(pIndex) # 获取当前页数据
    plist = p.page_range # 获取页面信息
    # 封装分页信息
    context = {'goodslist': list2, 'plist': plist, 'pIndex': pIndex}
    return render(request, "myadmin/goods/index.html", context)
