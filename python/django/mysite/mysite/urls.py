from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^polls/', include('polls.urls',
                                               namespace='polls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^forums/',
                           include('forums.urls', namespace='forums')),
                       url(r'^account/',
                           include('account.urls', namespace='account')),
                       )
