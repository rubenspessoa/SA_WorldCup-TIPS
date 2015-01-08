# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='time_steps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='timing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timing', models.TextField(null=True)),
                ('time_step', models.ForeignKey(to='time_steps.time_steps')),
                ('tweet', models.ForeignKey(to='tweets.Tweet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
