# Generated by Django 3.1.5 on 2022-08-30 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('field_query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery_list.grocerylist')),
            ],
        ),
    ]