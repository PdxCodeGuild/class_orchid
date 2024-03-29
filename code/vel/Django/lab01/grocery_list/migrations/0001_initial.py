# Generated by Django 4.1 on 2022-08-31 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
                ('completed_date', models.DateTimeField(blank=True, null=True, verbose_name='date completed')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
