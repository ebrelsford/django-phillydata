# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('external_data_sync', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhillyDataSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('healthy', models.BooleanField(default=True, help_text='Was synchronizing successful last attempt?', verbose_name='healthy')),
                ('ordering', models.IntegerField(default=1, help_text='The ordering of this source, lower numbers coming first.', verbose_name='ordering')),
                ('synchronize_in_progress', models.BooleanField(default=False, help_text='Is the source being synchronized right now?', verbose_name='synchronize in progress')),
                ('synchronize_frequency', models.IntegerField(help_text='The number of hours that should pass between synchronizations of this source.', null=True, verbose_name='synchronize frequency', blank=True)),
                ('next_synchronize', models.DateTimeField(help_text='The next time this data source should be synchronized.', null=True, verbose_name='next synchronize', blank=True)),
                ('last_synchronized', models.DateTimeField(help_text='The last time this data source was synchronized', verbose_name='last synchronized')),
                ('batch_size', models.IntegerField(help_text='The batch size that should be updated each time this source is synchronized', null=True, verbose_name='batch size', blank=True)),
                ('synchronizer_record', models.ForeignKey(blank=True, to='external_data_sync.SynchronizerRecord', help_text='The synchronizer to use with this data source.', null=True, verbose_name='synchronizer record')),
            ],
            options={
                'ordering': ('ordering',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
