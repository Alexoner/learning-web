from django.conf.urls import patterns, url
from forum import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'djangoByExample.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r"", views.main, name="main"),
                       url(r'^forum/(\d+)/$', views.forum, name="forum"),
                       url(r'^thread/(\d+)/$', views.thread, name="thread"),
                       # url(r'^post/(new_thread|replay)/(\d+)/$',
                       # views.post, 'post'),
                       # url(r'^reply/(\d+)/$', views.reply),
                       # url(r'^new_thread/(\d+)/$', 'new_thread'),
                       )
