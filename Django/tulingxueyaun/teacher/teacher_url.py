from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyaun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 子路由里视图函数只需函数名即可，无参数，也不需要从头开始匹配
    url(r'liudana/', views.do_app), # 4、在APP中处理
]