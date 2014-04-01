from django.conf.urls import patterns, url, include

from mysite.views import hello,current_datetime,hours_ahead

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$',hours_ahead),
    # url(r'^west/', include('west.urls')),
)
