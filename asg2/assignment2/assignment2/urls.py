from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assignment2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'home.views.index', name ='index'),
	url(r'^reset', 'home.views.reset', name='reset'),
	url(r'^login',	'home.views.login', name='login'),
	url(r'^register', 'home.views.register', name='register'),
	url(r'^admin/', include(admin.site.urls)),
)
