# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('waterdept', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterparcel',
            name='geometry',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True, verbose_name='geometry', blank=True),
            preserve_default=True,
        ),
    ]
