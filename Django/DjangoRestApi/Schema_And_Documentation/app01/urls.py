from django.conf.urls import url, include
from app01 import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter # 导入默认路由模块
from rest_framework.schemas import get_schema_view # 导入概要模块
from rest_framework.documentation import include_docs_urls # 导入文档模块

# 创建路由器并注册我们的视图
router = DefaultRouter()
router.register(r'publishers', views.PublisherViewSet)
router.register(r'books', views.BookViewSet)
# 实例化概要
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view), # 概要路径
    url(r'docs/', include_docs_urls(title="图书管理系统")), # 文档路径
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

