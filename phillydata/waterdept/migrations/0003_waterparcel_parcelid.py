# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waterdept', '0002_waterparcel_geometry'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterparcel',
            name='parcelid',
            field=models.IntegerField(help_text='The parcel ID assigned by the Water Dept', null=True, verbose_name='parcel id (int)', blank=True),
            preserve_default=True,
        ),
    ]
