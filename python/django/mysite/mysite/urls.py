from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^$', 'mysite.views.home', name='home'),
                       url(r'^polls/', include('polls.urls',
                                               namespace='polls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^forums/',
                           include('forums.urls', namespace='forums')),
                       url(r'^accounts/',
                           include('accounts.urls', namespace='accounts')),
                       # url(r'^accounts/',
                       # include('registration.backends.default.urls')),
                       #(r'^accounts/login/$', login),
                       #(r'^accounts/logout/$', logout),
                       )
