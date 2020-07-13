from django.conf.urls import url
from . import views

app_name = 'analysis'

urlpatterns = [
    url(r'^analysis/memory/$', views.memory, name='memory'),
    url(r'^analysis/memory/env/$', views.env, name='env'),
    url(r'^analysis/memory/proc1/$', views.proc1, name='proc1'),
    url(r'^analysis/memory/proc2/$', views.proc2, name='proc2'),
    url(r'^analysis/memory/proc3/$', views.proc3, name='proc3'),
    url(r'^analysis/memory/net/$', views.net, name='net'),
    url(r'^analysis/memory/files/$', views.files, name='files'),
    url(r'^analysis/memory/browser1/$', views.browser1, name='browser1'),
    url(r'^analysis/memory/browser2/$', views.browser2, name='browser2'),
    url(r'^analysis/memory/browser3/$', views.browser3, name='browser3'),
    url(r'^analysis/memory/cmd/$', views.cmd, name='cmd'),
    url(r'^analysis/memory/cmd2/$', views.cmd2, name='cmd2'),
    url(r'^analysis/memory/gui/$', views.gui, name='gui'),
    url(r'^analysis/memory/mal/$', views.mal, name='mal'),
    url(r'^analysis/memory/yara/$', views.yara, name='yara'),
    url(r'^analysis/memory/hashs/$', views.hashs, name='hashs'),
    url(r'^analysis/memory/mkatz/$', views.mkatz, name='mkatz'),
    url(r'^analysis/memory/proc_dump/(?P<p>[0-9]+)/$', views.proc_dump, name='proc_dump'),
    url(r'^analysis/memory/file_dump/(?P<Q>[0-9]+)/$', views.file_dump, name='file_dump'),

]
