# Generated by Django 3.2.6 on 2021-09-14 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_alter_restaurant_welcome_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
