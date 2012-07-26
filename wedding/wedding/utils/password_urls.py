"""
A URLconf module for views that allow admin users to reset passwords.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^reset/$',
        'django.contrib.auth.views.password_reset',
        name='password_reset'
    ),
    url(r'^reset/confirm/$',
        'django.contrib.auth.views.password_reset_done'
    ),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm'
    ),
    url(r'^reset/complete/$',
        'django.contrib.auth.views.password_reset_complete'
    ),
)
