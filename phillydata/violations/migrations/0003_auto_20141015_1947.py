# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('violations', '0002_violationtype_readable_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='violationtype',
            name='readable_description',
            field=models.CharField(help_text='The readable description for this type of violation.This description will be used if available.', max_length=200, null=True, verbose_name='readable description', blank=True),
        ),
    ]
