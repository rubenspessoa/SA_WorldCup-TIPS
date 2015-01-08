# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='sa_technique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.TextField(max_length=30)),
                ('description', models.TextField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sentiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sentiment', models.IntegerField()),
                ('sentiment_analysis_technique', models.ForeignKey(to='sentiment_analysis.sa_technique')),
                ('tweet', models.ForeignKey(to='tweets.Tweet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
