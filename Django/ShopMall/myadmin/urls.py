'''
ShopMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
'''
from django.conf.urls import include, url
from django.contrib import admin

#from .views import *
from . import views, viewsgoods
urlpatterns = [
    # url(r'^/', t),
    # url(r'^t3/', t3),

    # 后台用户管理
    url(r'^$', views.index, name="myadmin_index"),
    # 分页浏览信息
    url(r'^$', views.index, name="myadmin_index"),
    # 尖号表示以后面内容开头的表达式
    # 圆括号表示的是一个参数，里面的内容作为参数传递给被调用的函数
    # 参数名称以问好?加大写P开头，尖括号里面就是参数的名字
    # 尖括号后表示正则，[0-9]表示内容仅能是有0-9的数字构成，
    # 后面大括号{}表示出现的次数，此处4表示只能出现四个0-9的数字
    url(r'^users(?P<pIndex>[0-9]*)$', views.users, name="users"),
    # 后台用户管理
    url(r'^users$', views.usersindex, name="myadmin_usersindex"),
    url(r'^usersadd$', views.usersadd, name="myadmin_usersadd"),
    url(r'^usersinsert$', views.usersinsert, name="myadmin_usersinsert"),
    url(r'^usersdel/(?P<uid>[0-9]+)$', views.usersdel, name="myadmin_usersdel"),
    url(r'^usersedit/(?P<uid>[0-9]+)$', views.usersedit, name="myadmin_usersedit"),
    url(r'^usersupdate/(?P<uid>[0-9]+$)', views.usersupdate, name="myadmin_usersupdate"),
    # 后台管理员路由
    url(r'^login$', views.login, name="myadmin_login"),
    url(r'^dologin$', views.dologin, name="myadmin_dologin"),
    url(r'^logout$', views.logout, name="myadmin_logout"),
    # 验证码登陆的路由
    url(r'^verify$', views.verify, name="myadmin_verify"),

    # 后台商品类别信息管理
    url(r'^type$', viewsgoods.typeindex, name="myadmin_typeindex"),
    url(r'^typeadd/(?P<tid>[0-9]+)$', viewsgoods.typeadd, name="myadmin_typeadd"),
    url(r'^typeinsert$', viewsgoods.typeinsert, name="myadmin_typeinsert"),
    url(r'^typedel/(?P<tid>[0-9]+)$', viewsgoods.typedel, name="myadmin_typedel"),
    url(r'^typeedit/(?P<tid>[0-9]+)$', viewsgoods.typeedit, name="myadmin_typeedit"),
    url(r'^typeupdate/(?P<tid>[0-9]+)$', viewsgoods.typeupdate, name="myadmin_typeupdate"),

    # 商品信息管理
    url(r'^goods(?P<pIndex>[0-9]+)$', viewsgoods.goodsindex, name="myadmin_goodsindex"),
    url(r'^goodsadd$', viewsgoods.goodsadd, name="myadmin_goodsadd"),
    url(r'^goodsinsert$', viewsgoods.goodsinsert, name="myadmin_goodsinsert"),
    url(r'^goodsdel/(?P<gid>[0-9]+)$', viewsgoods.goodsdel, name="myadmin_goodsdel"),
    url(r'^goodsedit/(?P<gid>[0-9]+)$', viewsgoods.goodsedit, name="myadmin_goodsedit"),
    url(r'^goodsupdate/(?P<gid>[0-9]+)$', viewsgoods.goodsupdate, name="myadmin_goodsupdate"),

    # 订单信息管理
    url(r'^orders$', viewsgoods.ordersindex, name="myadmin_orders"),
    url(r'^ordersedit/(?P<oid>[0-9]+)$', viewsgoods.ordersedit, name="myadmin_ordersedit"),
    url(r'^ordersupdate/(?P<oid>[0-9]+)$', viewsgoods.ordersupdate, name="myadmin_ordersupdate"),





]
