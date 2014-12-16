import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import WaterParcel, waterparcel_mapping


def from_shapefile(transaction_mode='autocommit', **kwargs):
    """
    Load water parcel data into the database from the processed shapefile.
    """
    # Using transaction_mode=autocommit because otherwise LayerMapping gets
    # stuck on a feature and can't commit anything
    filename = os.path.join('water_parcels', 'water_parcels.shp')
    parcel_shp = get_processed_data_file(filename)
    mapping = LayerMapping(WaterParcel, parcel_shp, waterparcel_mapping,
                           transform=True, transaction_mode=transaction_mode)
    mapping.save(**kwargs)


def load(**kwargs):
    from_shapefile(**kwargs)
