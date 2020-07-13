from django.conf.urls import url
from . import views

app_name = 'network'

urlpatterns = [
    url(r'^analysis/network/$', views.network, name='network'),
    url(r'^analysis/network/files/$', views.file_dumps, name='file_dumps'),
    url(r'^analysis/network/http/$', views.http_traffic, name='http_traffic'),
]
