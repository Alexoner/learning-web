from django.conf.urls import url, patterns
from account import views

urlpatterns = patterns('',
                       url(r'^register/$', views.register, name='register'),
                       )
