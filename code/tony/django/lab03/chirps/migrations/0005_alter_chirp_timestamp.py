# Generated by Django 4.1.1 on 2022-09-10 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirps', '0004_alter_chirp_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chirp',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
