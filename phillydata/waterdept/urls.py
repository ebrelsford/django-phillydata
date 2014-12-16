from django.conf.urls import patterns, url

from .views import GeoJSONParcelListView


urlpatterns = patterns('',
    url(r'^geojson/', GeoJSONParcelListView.as_view(), name='waterparcel_geojson'),
)
