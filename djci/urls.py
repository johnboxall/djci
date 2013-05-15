from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from .views import home, signup

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$',  login, name='login'),
    url(r'^logout/$', logout, name='logout'),
)