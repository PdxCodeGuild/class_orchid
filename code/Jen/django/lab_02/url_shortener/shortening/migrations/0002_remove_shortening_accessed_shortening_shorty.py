# Generated by Django 4.1 on 2022-09-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortening', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortening',
            name='accessed',
        ),
        migrations.AddField(
            model_name='shortening',
            name='shorty',
            field=models.CharField(default='oops', max_length=20),
        ),
    ]