from django.conf.urls import patterns, include, url
from secSoftwareA2.views import *
from django.core.urlresolvers import reverse_lazy

#References:
#https://docs.djangoproject.com/en/1.7/_modules/django/contrib/auth/views/
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^update/$', update),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^/register/updatesuccess/$', update_success),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change'),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done',name="password_change_done"),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset'),
    url(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done', name="password_reset_done"),
    url(r'^password_reset_confirm/$', 'django.contrib.auth.views.password_reset_confirm', name="password_reset_confirm"),
    url(r'^password_reset_complete/$', 'password_reset_complete', name="password_reset_complete"),
    url(r'^home/$', home),
)