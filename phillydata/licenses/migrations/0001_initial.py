# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('li', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_type', models.CharField(max_length=32, null=True, verbose_name='contact type', blank=True)),
                ('company_name', models.CharField(max_length=300, null=True, verbose_name='company name', blank=True)),
                ('first_name', models.CharField(max_length=300, null=True, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=300, null=True, verbose_name='last name', blank=True)),
                ('address1', models.CharField(max_length=300, null=True, verbose_name='address1', blank=True)),
                ('address2', models.CharField(max_length=300, null=True, verbose_name='address2', blank=True)),
                ('city', models.CharField(max_length=300, null=True, verbose_name='city', blank=True)),
                ('state', models.CharField(max_length=100, null=True, verbose_name='state', blank=True)),
                ('zip_code', models.CharField(max_length=20, null=True, verbose_name='zip code', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issued_datetime', models.DateTimeField(help_text='When this license was issued', null=True, verbose_name='issued date/time', blank=True)),
                ('inactive_datetime', models.DateTimeField(help_text='When this license became inactive, if it is', null=True, verbose_name='inactive date/time', blank=True)),
                ('external_id', models.CharField(help_text="L&I's license number for this particular license", unique=True, max_length=30, verbose_name='external ID')),
                ('expires_month', models.CharField(help_text='The month this license will expire', max_length=30, null=True, verbose_name='month of expiry', blank=True)),
                ('expires_year', models.PositiveIntegerField(help_text='The year this license will expire', null=True, verbose_name='year of expiry', blank=True)),
                ('status', models.CharField(help_text='The last-known status of this license', max_length=30, null=True, verbose_name='status', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LicenseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text='The code L&I uses for this type of license.', unique=True, max_length=32, verbose_name='code')),
                ('name', models.TextField(help_text='The name L&I gives for this type of license.', verbose_name='name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='license',
            name='license_type',
            field=models.ForeignKey(to='licenses.LicenseType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='location',
            field=models.ForeignKey(to='li.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='primary_contact',
            field=models.ForeignKey(blank=True, to='licenses.Contact', help_text='The primary contact for this license', null=True),
            preserve_default=True,
        ),
    ]
