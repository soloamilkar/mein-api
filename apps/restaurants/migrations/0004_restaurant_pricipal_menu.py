# Generated by Django 3.2.6 on 2021-08-31 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_restaurant_max_tables'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='pricipal_menu',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]