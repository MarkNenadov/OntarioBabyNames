from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url( r'^web/', include('web.urls')),
    # Examples:
    # url(r'^$', 'babynames.views.home', name='home'),
    # url(r'^babynames/', include('babynames.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
