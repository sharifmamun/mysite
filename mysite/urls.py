from django.conf.urls import patterns, include, url
from mysite.views import current_datetime

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^time/$', current_datetime),
)
