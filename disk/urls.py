from django.conf.urls import url
from . import views

app_name = 'disk'

urlpatterns = [
    url(r'^analysis/disk/$', views.disk, name='disk'),
    url(r'^analysis/disk/dumped/$', views.dumped_files, name='dumped_files'),
    url(r'^analysis/disk/deleted/$', views.deleted_files, name='deleted_files'),

]
