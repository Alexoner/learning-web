from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

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
                       # url(r'^accounts/',
                       # include('registration.backends.default.urls')),
                       (r'^accounts/login/$', login),
                       (r'^accounts/logout/$', logout),
                       (r'^accounts/register/$', CreateView(
                        template_name='register.html',
                        form_class=UserCreationForm,
                        success_url='/polls/index/'))
                       )
