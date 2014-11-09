from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'djangoByExample.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r"", "views.main", "main"),
                       url(r'^forum/(\d+)/$', "forum"),
                       url(r'^thread/(\d+)/$', "thread"),
                       )
