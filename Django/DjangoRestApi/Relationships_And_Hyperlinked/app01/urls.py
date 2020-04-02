from django.conf.urls import url, include
from app01 import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.api_root),

    url(r'^publishers/$', views.PublisherList.as_view(), name="publisher-list"),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view(), name="publisher-detail"),
    url(r'^books/$', views.BookList.as_view(), name="book-list"),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name="bool-detail"),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)