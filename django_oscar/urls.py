from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('django_oscar.app.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'reponame', 'get_reponame', name='reponame'),

    url(r'^admin/', include(admin.site.urls)),
)
