from django.conf.urls import patterns, url

from .views import GeoJSONPolygonView


urlpatterns = patterns('',
    url(r'^geojson/', GeoJSONPolygonView.as_view(), name='waterparcel_geojson'),
)
