# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centroid', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='centroid')),
                ('asset_id', models.CharField(null=True, max_length=10, blank=True, help_text='The asset ID', unique=True, verbose_name='asset id')),
                ('mapreg', models.CharField(help_text="The parcel's registry number", max_length=10, null=True, verbose_name='mapreg', blank=True)),
                ('address', models.CharField(help_text="The parcel's address", max_length=200, null=True, verbose_name='address', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('agency', models.CharField(help_text='The agency that holds this parcel', max_length=20, null=True, verbose_name='agency', blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, blank=True, help_text='The price of this property', null=True, verbose_name='price')),
                ('price_str', models.CharField(help_text='The price string for this property--does not always match the numeric price', max_length=50, null=True, verbose_name='price string', blank=True)),
                ('area', models.DecimalField(decimal_places=2, max_digits=15, blank=True, help_text='The area of this property in square feet', null=True, verbose_name='area')),
                ('status', models.CharField(default=b'new and available', max_length=30, verbose_name='status', choices=[(b'new and available', b'new and available'), (b'available', b'available'), (b'no longer available', b'no longer available')])),
                ('added', models.DateTimeField(help_text=b'The first time this property was seen in the available propery list', verbose_name='date added', auto_now_add=True)),
                ('last_seen', models.DateTimeField(help_text=b'The last time this property was seen in the available propery list', verbose_name='date last seen')),
            ],
            options={
                'verbose_name': 'available property',
                'verbose_name_plural': 'available properties',
            },
            bases=(models.Model,),
        ),
    ]
