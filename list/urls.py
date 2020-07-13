from django.conf.urls import url
from . import views

app_name = 'list'

urlpatterns = [
    url(r'^list$', views.list, name='list'),
    url(r'^list/ready/(?P<id>[0-9]+)/$', views.ready, name='ready'),
    url(r'^list/add$', views.add_case, name='add_case'),
    url(r'^list/delete/(?P<id>[0-9]+)/$', views.delete_case, name='delete_case'),
    url(r'^$', views.login_user, name='login_user'),
    url(r'^logout$', views.logout_user, name='logout_user'),
]
