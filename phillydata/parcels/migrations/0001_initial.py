# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, verbose_name='geometry')),
                ('basereg', models.CharField(help_text='The registry number which there is a deed attached to.', max_length=10, null=True, verbose_name='basereg', blank=True)),
                ('mapreg', models.CharField(help_text='A registry number that may or may not specifically have a deed attached to it.', max_length=10, null=True, verbose_name='mapreg', blank=True)),
                ('stcod', models.CharField(help_text='Street code. Maintained by the Department of Streets.', max_length=10, null=True, verbose_name='stcod', blank=True)),
                ('address', models.CharField(help_text='The street address, created by concatenating house number and street fields from the parcel database.', max_length=300, null=True, verbose_name='address', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
