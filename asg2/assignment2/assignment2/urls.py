from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assignment2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'assignment2.views.index', name ='index'),
	url(r'^reset', 'assignment2.views.reset', name='reset'),
	url(r'^login',	'assignment2.views.login', name='login'),
	url(r'^register', 'assignment2.views.register', name='register'),
	url(r'^admin/', include(admin.site.urls)),
)
