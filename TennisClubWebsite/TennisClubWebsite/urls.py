from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                           # url(r'^$', 'TennisClubSite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^ladder/', include('ladder.urls',namespace="ladder")),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^admin', include(admin.site.urls)),
                       url(r'^base', base),
                       url(r'^index$',index),
                       url(r'^about$',about),
                       url(r'^news$',news),
                       url(r'^roster$',roster),
                       url(r'^media$',media),
                       url(r'^faq$',faq),
                       url(r'^contact$',contact),
                       url(r'', homepage),
                       )
