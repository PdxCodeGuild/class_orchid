# Generated by Django 4.1 on 2022-08-30 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completion_date',
            field=models.DateTimeField(null=True, verbose_name='completion date'),
        ),
    ]
