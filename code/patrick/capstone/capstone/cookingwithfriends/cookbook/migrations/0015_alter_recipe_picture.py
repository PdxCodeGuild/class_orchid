# Generated by Django 4.1 on 2022-10-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0014_alter_recipe_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, default='default2.jpg', upload_to='images'),
        ),
    ]
