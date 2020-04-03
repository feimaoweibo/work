from django.conf.urls import url, include
from app01 import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
# 使用viewset方式的路由

book_list = views.BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

book_detail = views.BookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
'''
# 创建路由器并注册我们的视图

router = DefaultRouter()
router.register(r'^books/$', views.BookViewSet)
'''
urlpatterns = [
    url(r'^$', views.api_root),

    url(r'^publishers/$', views.PublisherList.as_view(), name="publisher-list"),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view(), name="publisher-detail"),
    #url(r'^books/$', views.BookList.as_view(), name="book-list"),
    #url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name="bool-detail"),

    # 使用viewset方式的路由
    url(r'^books/$', book_list, name="book-list"),
    url(r'^books/(?P<pk>[0-9]+)/$', book_detail, name="bool-detail"),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)