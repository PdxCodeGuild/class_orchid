# Generated by Django 4.1.1 on 2022-10-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0007_alter_recipe_pricefilter'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, height_field=100, null=True, upload_to='', width_field=100),
        ),
    ]
