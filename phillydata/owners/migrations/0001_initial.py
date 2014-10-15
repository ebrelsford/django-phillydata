# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=256, verbose_name='code')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256, verbose_name='name')),
            ],
            options={
                'verbose_name': 'alias',
                'verbose_name_plural': 'aliases',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256, verbose_name='name')),
                ('owner_type', models.CharField(default=b'private', max_length=20, verbose_name='owner type', choices=[(b'private', b'private'), (b'public', b'public'), (b'unknown', b'unknown')])),
                ('agency_codes', models.ManyToManyField(help_text='Agency codes used to refer to this owner', to='owners.AgencyCode', null=True, verbose_name='agency codes', blank=True)),
                ('aliases', models.ManyToManyField(help_text='Other names for this owner', to='owners.Alias', null=True, verbose_name='aliases', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
