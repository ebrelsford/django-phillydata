# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandUseArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, verbose_name='geometry')),
                ('object_id', models.CharField(help_text='The object ID (OBJECTID)', unique=True, max_length=15, verbose_name='object ID')),
                ('category', models.CharField(help_text='The land use category (C_DIG1DESC)', max_length=30, null=True, verbose_name='category', blank=True)),
                ('subcategory', models.CharField(help_text='The land use subcategory (C_DIG2DESC)', max_length=30, null=True, verbose_name='subcategory', blank=True)),
                ('description', models.CharField(help_text='The land use description (C_DIG3DESC)', max_length=30, null=True, verbose_name='description', blank=True)),
                ('vacant_building', models.CharField(help_text='(VACBLDG)', max_length=10, null=True, verbose_name='vacant building', blank=True)),
                ('area', models.DecimalField(decimal_places=2, max_digits=15, blank=True, help_text='The area of this parcel in square feet', null=True, verbose_name='area')),
                ('added', models.DateTimeField(help_text=b'The first time this area was seen in the data source', verbose_name='date added', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
