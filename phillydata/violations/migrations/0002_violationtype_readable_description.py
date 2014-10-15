# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('violations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='violationtype',
            name='readable_description',
            field=models.CharField(help_text='The readable description for this type of violation.', max_length=200, null=True, verbose_name='readable description', blank=True),
            preserve_default=True,
        ),
    ]
