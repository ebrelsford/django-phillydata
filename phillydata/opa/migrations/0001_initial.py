# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountOwner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256, verbose_name='name')),
                ('owner', models.ForeignKey(verbose_name='owner', blank=True, to='owners.Owner', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillingAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('external_id', models.CharField(help_text='The OPA account number (also called "BRT number")', unique=True, max_length=50, verbose_name='external id')),
                ('property_address', models.CharField(help_text='The address of the property this account is associated with', max_length=300, null=True, verbose_name='property address', blank=True)),
                ('improvement_description', models.CharField(help_text='The improvement description according to OPA', max_length=300, null=True, verbose_name='improvement description', blank=True)),
                ('sale_date', models.DateField(help_text='The date of the last sale of this property according to the OPA', null=True, verbose_name='sale date', blank=True)),
                ('land_area', models.DecimalField(decimal_places=3, max_digits=20, blank=True, help_text='The land area of the property according to the OPA in square feet', null=True, verbose_name='land area (sq ft)')),
                ('improvement_area', models.IntegerField(help_text='The improvement area of the property according to the OPA', null=True, verbose_name='improvement area', blank=True)),
                ('assessment', models.DecimalField(decimal_places=2, max_digits=20, blank=True, help_text='The assessment of the property according to the OPA', null=True, verbose_name='assessment')),
                ('mailing_name', models.CharField(help_text='The name on the mailing address for this account.', max_length=300, null=True, verbose_name='mailing name', blank=True)),
                ('mailing_address', models.CharField(help_text='The mailing address for this account.', max_length=300, null=True, verbose_name='mailing address', blank=True)),
                ('mailing_postal_code', models.CharField(max_length=10, null=True, verbose_name='mailing postal code', blank=True)),
                ('mailing_city', models.CharField(max_length=50, null=True, verbose_name='mailing city', blank=True)),
                ('mailing_state_province', models.CharField(max_length=40, null=True, verbose_name='mailing state/province', blank=True)),
                ('mailing_country', models.CharField(default=b'USA', max_length=40, null=True, verbose_name='mailing country', blank=True)),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('account_owner', models.ForeignKey(verbose_name='account owner', blank=True, to='opa.AccountOwner', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
