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
]
