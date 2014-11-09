from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'djangoByExample.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^todo/',
                           include('todo.urls', namespace="todo")),
                       url(r'^mark_done/(\d*)/$', "todo.views.mark_done"),
                       # url(r'^item_action/(done|delete|onhold)/(\d*)/$',
                       #"item_action"),
                       )
