
from django.conf.urls import patterns, include, url

from tastypie.api import Api

from django.contrib import admin
admin.autodiscover()

from dzapgo.resources import HookResource
v1_api = Api(api_name='v1')
v1_api.register(HookResource())


urlpatterns = patterns('',
    url(r'^$', 'notes.views.homepage', name="homepage"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
