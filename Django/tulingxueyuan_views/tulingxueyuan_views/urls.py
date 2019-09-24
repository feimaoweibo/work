from django.conf.urls import include, url
from django.contrib import admin

from teacher_app import views as v
urlpatterns = {
    # Examples:
    # url(r'^$', 'tulingxueyuan_views.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^teacher/', v.teacher),  # 2、简单视图
    url(r'^v2_exp/', v.v2_exception),  # http404异常案例

    # 4、HttpResponseRedirect重定向
    url(r'^v10_1/', v.v10_1),
    url(r'^v10_2/', v.v10_2),
    url(r'^v11/', v.v11, name="v11"),

    # 5、Request对象get()方法案例
    url(r'^v8/', v.v8_get),


    # 5、Request对象post()方法案例
    url(r'^v9_get', v.v9_get),
    url(r'^v9_post', v.v9_post),
    # 5、Request对象render手动编写视图案例
    url(r'^render_test/', v.render_test),
    url(r'^render2_test/', v.render2_test),
    url(r'^render3_test/', v.render3_test),
    url(r'^render_to_request/', v.render_to_request),
    # 5、Request对象系统内建视图案例
    url(r'^get404/', v.get404),

}
