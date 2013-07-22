from django.conf.urls import patterns, url

from web import views

urlpatterns = patterns('',
        # /web/
        url( r'^$', views.index, name='index' ),

        # /web/name
        url( r'^(?P<nameId>\d+)/$', views.nameDetails, name="nameDetails" )
)
