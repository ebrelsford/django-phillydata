# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_name', models.CharField(max_length=256, verbose_name='owner name')),
                ('owner_name2', models.CharField(max_length=256, verbose_name='owner name #2')),
                ('brt_number', models.CharField(unique=True, max_length=10, verbose_name='BRT number')),
                ('property_address', models.CharField(help_text='The property address for this account.', max_length=300, null=True, verbose_name='property address', blank=True)),
                ('property_city', models.CharField(max_length=50, null=True, verbose_name='property city', blank=True)),
                ('property_state_province', models.CharField(max_length=40, null=True, verbose_name='property state/province', blank=True)),
                ('property_postal_code', models.CharField(max_length=10, null=True, verbose_name='property postal code', blank=True)),
                ('building_description', models.CharField(max_length=100, null=True, verbose_name='building description', blank=True)),
                ('building_category', models.CharField(max_length=100, null=True, verbose_name='building category', blank=True)),
                ('amount_delinquent', models.DecimalField(decimal_places=2, max_digits=15, blank=True, help_text='The amount this account is delinquent', null=True, verbose_name='amount delinquent')),
                ('years_delinquent', models.IntegerField(help_text='Count_of_Years from the delinquency data source', null=True, verbose_name='years delinquent', blank=True)),
                ('min_period', models.DateField(help_text='Min_Period from the delinquency data source, presumably when the account entered delinquency', null=True, verbose_name='min period', blank=True)),
                ('max_period', models.DateField(help_text='Max_Period from the delinquency data source, presumably when the account left delinquency', null=True, verbose_name='max period', blank=True)),
                ('taxable_assessment', models.DecimalField(null=True, verbose_name='taxable assessment', max_digits=15, decimal_places=2, blank=True)),
                ('exempt_abate_assessment', models.DecimalField(null=True, verbose_name='exempt abate assessment', max_digits=15, decimal_places=2, blank=True)),
                ('market_value', models.DecimalField(null=True, verbose_name='market value', max_digits=15, decimal_places=2, blank=True)),
                ('last_updated', models.DateField(help_text='The date this data was collected', null=True, verbose_name='last updated', blank=True)),
                ('billing_account', models.ForeignKey(verbose_name='billing account', blank=True, to='opa.BillingAccount', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
