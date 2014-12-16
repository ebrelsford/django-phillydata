import json
import geojson

from django.contrib.gis.geos import Polygon

from inplace.boundaries.models import Layer
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


class FindParcelView(GeoJSONListView):

    def get_feature(self, parcel):
        try:
            zipcodes = Layer.objects.get(name='zipcodes')
            zipcode = zipcodes.boundary_set.get(
                geometry__contains=parcel.geometry,
            ).label
        except Exception:
            zipcode = ''

        return geojson.Feature(
            parcel.id,
            geometry=geojson.MultiPolygon(
                coordinates=parcel.geometry.coords,
            ),
            properties={
                'address': parcel.address,
                'lot_count': parcel.lot_set.count(),
                'zipcode': zipcode,
            },
        )

    def get_queryset(self):
        parcels = WaterParcel.objects.filter(geometry__isnull=False)

        try:
            return parcels.filter(pk=self.request.GET['pk'])
        except Exception:
            try:
                return parcels.filter(
                    address__icontains=self.request.GET['address']
                )
            except Exception:
                pass

        return None
