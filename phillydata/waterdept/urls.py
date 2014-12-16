from django.conf.urls import patterns, url

from .views import (FindParcelView, GeoJSONParcelDetailView,
                    GeoJSONParcelListView)


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/geojson/', GeoJSONParcelDetailView.as_view(),
        name='waterparcel_detail_geojson'),
    url(r'^find/geojson/', FindParcelView.as_view(), name='waterparcel_find'),
    url(r'^geojson/', GeoJSONParcelListView.as_view(), name='waterparcel_geojson'),
)
