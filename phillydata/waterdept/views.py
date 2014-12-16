import json
import geojson

from django.contrib.gis.geos import Polygon

from inplace.views import GeoJSONDetailView, GeoJSONListView
from .models import WaterParcel


class GeoJSONParcelMixin(object):

    def get_feature(self, parcel):
        return geojson.Feature(
            parcel.pk,
            geometry=json.loads(parcel.geojson),
            properties=self.get_properties(parcel),
        )

    def get_properties(self, parcel):
        return {
            'address': parcel.address,
        }


class GeoJSONParcelDetailView(GeoJSONParcelMixin, GeoJSONDetailView):
    model = WaterParcel

    def get_queryset(self):
        return WaterParcel.objects.filter(geometry__isnull=False) \
                .geojson(precision=6)


class GeoJSONParcelListView(GeoJSONParcelMixin, GeoJSONListView):
    model = WaterParcel

    def get_queryset(self):
        try:
            bbox = Polygon.from_bbox(self.request.GET['bbox'].split(','))
            return super(GeoJSONParcelListView, self).get_queryset().filter(
                geometry__intersects=bbox,
            ).geojson(precision=6)
        except KeyError:
            return WaterParcel.objects.none()
