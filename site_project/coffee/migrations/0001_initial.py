# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coffee_count', models.IntegerField(default=0)),
                ('consumption_date', models.DateTimeField(verbose_name=b'date consumed')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
