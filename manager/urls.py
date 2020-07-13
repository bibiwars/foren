from django.conf.urls import url
from . import views

app_name = 'manager'

urlpatterns = [
    url(r'^manager/$', views.index, name='index'),
    url(r'^manager/users/$', views.users, name='users'),
    url(r'^manager/users/add$', views.user_add, name='user_add'),
    url(r'^manager/users/remove/(?P<user>[a-zA-Z]+)/$', views.user_remove, name='user_remove'),
    url(r'^manager/users/change/(?P<user>[a-zA-Z]+)/$', views.user_ch, name='user_ch'),
    url(r'^manager/users/change/gen/(?P<user>[a-zA-Z]+)/$', views.user_ch_gen, name='user_ch_gen'),
    url(r'^manager/users/change/pwd/(?P<user>[a-zA-Z]+)/$', views.user_ch_pwd, name='user_ch_pwd'),
    url(r'^manager/users/$', views.groups, name='groups'),
    url(r'^manager/groups/change/(?P<grp>[a-zA-Z]+)/$', views.group_ch, name='group_ch'),
    url(r'^manager/clears/$', views.clears, name='clears'),
]