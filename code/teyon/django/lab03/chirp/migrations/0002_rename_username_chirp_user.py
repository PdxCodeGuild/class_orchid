# Generated by Django 4.1 on 2022-09-13 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chirp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chirp',
            old_name='username',
            new_name='user',
        ),
    ]
