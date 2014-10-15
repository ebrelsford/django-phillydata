# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDistrict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, verbose_name='geometry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ZoningType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, verbose_name='code')),
                ('long_code', models.CharField(max_length=30, verbose_name='long code')),
                ('group', models.CharField(max_length=100, verbose_name='group')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
            ],
            options={
                'ordering': ('code',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='basedistrict',
            name='zoning_type',
            field=models.ForeignKey(verbose_name='zoning type', to='zoning.ZoningType'),
            preserve_default=True,
        ),
    ]
