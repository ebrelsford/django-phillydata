# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='point')),
                ('address', models.CharField(help_text='The street address, created by concatenating house number and street fields.', max_length=300, null=True, verbose_name='address', blank=True)),
                ('zip_code', models.CharField(max_length=20, null=True, verbose_name='zip code', blank=True)),
                ('external_id', models.CharField(help_text="The ID of this location in L&I's API", unique=True, max_length=30, verbose_name='external ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
