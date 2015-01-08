# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='pp_technique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pre_processed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pre_processed', models.TextField(max_length=180)),
                ('pre_process_technique', models.ForeignKey(to='pre_process.pp_technique')),
                ('tweet', models.ForeignKey(to='tweets.Tweet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
