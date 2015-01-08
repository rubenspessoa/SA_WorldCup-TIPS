# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='geolocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.TextField(null=True)),
                ('geo', models.TextField(null=True)),
                ('coordinates', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='geolocation_relation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geolocation', models.ForeignKey(to='geolocation.geolocation')),
                ('tweet', models.ForeignKey(to='tweets.Tweet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
