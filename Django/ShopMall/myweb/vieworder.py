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
        ob.email = request.POST['email']
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

# 购物车的添加
def addshopcart(request,sid):
    # 获取要放入购物车中的商品信息
    goods = Goods.objects.get(id=sid)
    shop = goods.dePosit()
    print(shop)
    shop['m'] = int(request.POST['m'])
    # 从session中获取购物车信息
    if 'shoplist' in request.session:
        shoplist = request.session['shoplist']
    else:
        shoplist = {}
    # 判断商品是否在购物车中
    if sid in shoplist:
        # 商品数量加一
        shoplist[sid]['m'] += shop['m']
    else:
        # 新商品添加
        shoplist[sid] = shop
    # 将购物车信息放回到session中
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopcart'))

# 购物车数量改变
def changeshopcart(request):
    context = loadinfo()
    shoplist = request.session['shoplist']
    shopid = request.GET['sid']
    num = int(request.GET['num'])
    if num < 1:
        num = 1
    shoplist[shopid]['m'] = num
    request.session['shoplist'] = shoplist
    return render(request, "myweb/shopcart.html", context)

# 购物车的删除
def delshopcart(request,sid):
    shoplist = request.session['shoplist']
    del shoplist[sid]
    request.session['shoplist'] = shoplist
    # 跳转登录页面（url地址改变）
    return redirect(reverse('shopcart'))

# 购物车清空
def clearshopcart(request):
    shoplist = request.session['shoplist']
    request.session['shoplist'] = {}
    return redirect(reverse('shopcart'))


# 订单信息显示页面
def indent(request):
    context = loadinfo()
    # 从session中获取登录者的id号，并且从订单表order中获取当前用户的所有订单
    orders = Orders.objects.filter(uid=request.session['user']['id'])
    # 遍历当前用户的所有订单属性，并获得对应的订单详情信息
    for order in orders:
        dlist = Detail.objects.filter(orderid=order.id)
        order.dedail_list = dlist
        # 追加1图片信息
        for detail in dlist:
            goods = Goods.objects.get(id=detail.goodsid)
            detail.picname = goods.picname
    context['orders'] = orders
    context['dlist'] = dlist
    return render(request, "myweb/indent.html", context)
