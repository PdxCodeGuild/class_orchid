# Generated by Django 4.1 on 2022-09-02 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0002_review_item_item_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.RemoveField(
            model_name='item',
            name='inquiry',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_text',
        ),
        migrations.AddField(
            model_name='item',
            name='checked_item',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='grocery_item',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Inquiry',
        ),
    ]
