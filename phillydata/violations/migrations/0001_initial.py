# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('li', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('violation_datetime', models.DateTimeField(null=True, verbose_name='date/time', blank=True)),
                ('external_id', models.CharField(help_text="The ID of this violation in L&I's API", unique=True, max_length=30, verbose_name='external ID')),
                ('case_number', models.CharField(help_text="The case number of this violation in L&I's API", max_length=30, null=True, verbose_name='case number', blank=True)),
                ('location', models.ForeignKey(to='li.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ViolationLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='point')),
                ('address', models.CharField(help_text='The street address, created by concatenating house number and street fields from the violation.', max_length=300, null=True, verbose_name='address', blank=True)),
                ('zip_code', models.CharField(max_length=20, null=True, verbose_name='zip code', blank=True)),
                ('external_id', models.CharField(help_text="The ID of this location in L&I's API", unique=True, max_length=30, verbose_name='external ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ViolationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text='The code L&I uses for this type of violation.', unique=True, max_length=32, verbose_name='code')),
                ('li_description', models.TextField(help_text='The description L&I gives for this type of violation.', verbose_name='L&I description')),
                ('full_description', models.TextField(help_text='A longer description of this type of violation.', null=True, verbose_name='full description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='violation',
            name='violation_type',
            field=models.ForeignKey(to='violations.ViolationType'),
            preserve_default=True,
        ),
    ]
