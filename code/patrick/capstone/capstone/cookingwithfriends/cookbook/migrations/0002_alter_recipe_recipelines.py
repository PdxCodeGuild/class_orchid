# Generated by Django 4.1.1 on 2022-10-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipelines',
            field=models.TextField(),
        ),
    ]
