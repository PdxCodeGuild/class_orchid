# Generated by Django 4.1.1 on 2022-10-05 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0005_alter_recipe_pricefilter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pricefilter',
            field=models.CharField(choices=[('$', '$'), ('$$', '$$'), ('$$$', '$$$')], default='two', max_length=5),
        ),
    ]
