from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('mmo.apps.site.urls', namespace='home')),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'site/login.html',
    }),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),

    url(r'^character/', include('mmo.apps.characters.urls', namespace='character')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
