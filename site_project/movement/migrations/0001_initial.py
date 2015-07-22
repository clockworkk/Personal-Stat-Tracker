# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateTimeField(verbose_name=b'date of entry')),
                ('steps', models.IntegerField(default=0)),
                ('distance', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Fitbit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateTimeField(verbose_name=b'date of entry')),
                ('steps', models.IntegerField(default=0)),
                ('distance', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('weight', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('active_minutes', models.IntegerField(default=0)),
            ],
        ),
    ]
