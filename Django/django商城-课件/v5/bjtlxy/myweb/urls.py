"""bjtlxy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views, vieworder

urlpatterns = [
    # 登陆注册页面的路由
    # 跳转登陆页面
    url(r'^login$', views.login, name="login"),
    url(r'^dologin$', views.dologin, name="dologin"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^register$', views.register, name="register"),
    url(r'^doregister$', views.doregister, name="doregister"),
    # 个人中心页面路由
    url(r'^personal$', vieworder.personal, name="personal"),
    url(r'^peredit$', vieworder.peredit, name="peredit"),
    url(r'^perupdate$', vieworder.perupdate, name="perupdate"),

    # 购物车页面
    url(r'^shopcart$', vieworder.shopcart, name="shopcart"),
    url(r'^addshopcart/(?P<sid>[0-9]+)$', vieworder.addshopcart, name="addshopcart"),
    url(r'^changeshopcart$', vieworder.changeshopcart, name="changeshopcart"),
    url(r'^delshopcart/(?P<sid>[0-9]+)$', vieworder.delshopcart, name="delshopcart"),
    url(r'^clearshopcart$', vieworder.clearshopcart, name="clearshopcart"),

    # 我的订单路由
    # 访问订单表单页
    url(r'^myorder$', vieworder.myorder, name="myorder"),
    # 订单信息确认
    url(r'^myorderaffirm$', vieworder.myorderaffirm, name="myorderaffirm"),
    # 订单信息添加
    url(r'^myorderadd$', vieworder.myorderadd, name="myorderadd"),

    # 我的订单
    url(r'^indent$', vieworder.indent, name="indent"),
    # 取消订单
    url(r'^indentdel/(?P<oid>[0-9]+)$', vieworder.indentdel, name="indentdel"),

]
