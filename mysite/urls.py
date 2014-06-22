from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
from mysite.views import hello,current_datetime,hours_ahead

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'blog.views.index'),
    (r'^(?P<slug>[\w\-]+)/$','blog.views.post'),
    # (r'^hello/$', hello),
    # (r'^time/$', current_datetime),
    # (r'^time/plus/(\d{1,2})/$',hours_ahead),
    # (r'^index/$', 'blog.views.index'),
)
