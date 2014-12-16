import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import WaterAccount, WaterParcel, waterparcel_mapping


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


def fix_water_accounts():
    """Fix WaterAccount instances that point to old WaterParcels."""
    old_accounts = WaterAccount.objects.filter(water_parcel__parcelid__isnull=True)
    for water_account in old_accounts:
        orig_parcel = water_account.water_parcel

        try:
            # Find new WaterParcel
            new_parcel = WaterParcel.objects.get(parcelid=orig_parcel.parcel_id)

            # Update new WaterParcel with missing data from old WaterParcel
            for field in orig_parcel._meta.fields:
                attrname = field.get_attname()
                if not getattr(new_parcel, attrname):
                    setattr(new_parcel, attrname, getattr(orig_parcel, attrname))
            new_parcel.save()

            # Point account to new parcel
            water_account.water_parcel = new_parcel
            water_account.save()
        except WaterParcel.DoesNotExist:
            print 'Could not find WaterParcel %s. Moving on.' % orig_parcel.parcel_id
            continue
