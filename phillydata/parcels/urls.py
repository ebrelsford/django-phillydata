from django.conf.urls import patterns, url

from .views import FindParcelView


urlpatterns = patterns('',
    url(r'^geojson/', FindParcelView.as_view(), name='find_parcel'),
)
