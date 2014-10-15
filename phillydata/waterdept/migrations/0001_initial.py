# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_id', models.CharField(help_text='The ID of this account with the Water Department', max_length=30, null=True, verbose_name='account ID', blank=True)),
                ('account_number', models.CharField(help_text='A slightly expanded version of the account ID', max_length=30, null=True, verbose_name='account number', blank=True)),
                ('customer_id', models.CharField(help_text='The ID for this customer with the Water Department', max_length=20, null=True, verbose_name='customer ID', blank=True)),
                ('customer_name', models.CharField(max_length=100, null=True, verbose_name='customer name', blank=True)),
                ('inst_id', models.CharField(max_length=20, null=True, verbose_name='inst ID', blank=True)),
                ('account_status', models.CharField(help_text='Discontinued / Current', max_length=30, null=True, verbose_name='account status', blank=True)),
                ('account_status_abbreviation', models.CharField(max_length=10, null=True, verbose_name='account status abbreviation', blank=True)),
                ('meter_size', models.CharField(max_length=30, null=True, verbose_name='meter size', blank=True)),
                ('meter_size_abbreviation', models.CharField(max_length=10, null=True, verbose_name='meter size abbreviation', blank=True)),
                ('service_type', models.CharField(max_length=10, null=True, verbose_name='service type', blank=True)),
                ('service_type_label', models.CharField(max_length=50, null=True, verbose_name='service type label', blank=True)),
                ('stormwater_status', models.CharField(help_text='Billed / Not Billed', max_length=30, null=True, verbose_name='stormwater status', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WaterParcel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parcel_id', models.CharField(help_text='The parcel ID assigned by the Water Dept', max_length=20, null=True, verbose_name='parcel id', blank=True)),
                ('brt_account', models.CharField(help_text='The OPA/BRT account according to the Water Dept', max_length=20, null=True, verbose_name='BRT account', blank=True)),
                ('ten_code', models.CharField(max_length=20, null=True, verbose_name='ten code', blank=True)),
                ('owner1', models.CharField(max_length=256, null=True, verbose_name='owner1', blank=True)),
                ('owner2', models.CharField(max_length=256, null=True, verbose_name='owner1', blank=True)),
                ('address', models.CharField(max_length=256, null=True, verbose_name='address', blank=True)),
                ('gross_area', models.DecimalField(decimal_places=2, max_digits=20, blank=True, help_text='The area of the parcel in square feet', null=True, verbose_name='gross area')),
                ('impervious_area', models.DecimalField(decimal_places=2, max_digits=20, blank=True, help_text='The impervious area of the parcel in square feet', null=True, verbose_name='impervious area')),
                ('building_type', models.CharField(max_length=50, null=True, verbose_name='building type', blank=True)),
                ('building_description', models.CharField(max_length=100, null=True, verbose_name='building description', blank=True)),
                ('building_code', models.CharField(max_length=20, null=True, verbose_name='building code', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='wateraccount',
            name='water_parcel',
            field=models.ForeignKey(verbose_name='water parcel', to='waterdept.WaterParcel'),
            preserve_default=True,
        ),
    ]
