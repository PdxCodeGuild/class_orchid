# Generated by Django 4.1 on 2022-08-31 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateTimeField(verbose_name='date completed'),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created'),
        ),
    ]