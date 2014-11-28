from django.conf.urls import patterns, include, url
from django.contrib import admin
from djlogweb.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', base_view.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', post_view.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
