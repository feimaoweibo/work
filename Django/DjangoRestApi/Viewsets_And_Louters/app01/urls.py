from django.conf.urls import url, include
from app01 import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
# 创建路由器并注册我们的视图
router = DefaultRouter()
router.register(r'publishers', views.PublisherViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

#urlpatterns = format_suffix_patterns(urlpatterns)