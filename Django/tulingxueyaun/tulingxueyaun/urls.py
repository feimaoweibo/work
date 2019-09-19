from django.conf.urls import include, url
from django.contrib import admin

from teacher import views as tv
from teacher import teacher_url
urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyaun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 视图函数只需要有函数名即可，不需要参数
    url(r'^normalmap/', tv.do_normalmap), # 2、正常映射

    # 尖号表示以后面内容开头的表达式
    # 圆括号表示的是一个参数，里面的内容作为参数传递给被调用的函数
    # 参数名称以问好?加大写P开头，尖括号里面就是参数的名字
    # 尖括号后表示正则，[0-9]表示内容仅能是有0-9的数字构成，
    # 后面大括号{}表示出现的次数，此处4表示只能出现四个0-9的数字
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.withparam), # 3、URL中带参数映射
    url(r'^teacher/', include(teacher_url)),
]
