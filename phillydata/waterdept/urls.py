from django.conf.urls import patterns, url

from .views import GeoJSONParcelDetailView, GeoJSONParcelListView


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/geojson/', GeoJSONParcelDetailView.as_view(),
        name='waterparcel_detail_geojson'),
    url(r'^geojson/', GeoJSONParcelListView.as_view(), name='waterparcel_geojson'),
)
