from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from wedding import views


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^RSVP/$', views.RSVP.as_view(), name='rsvp'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()