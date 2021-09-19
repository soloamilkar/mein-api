# Generated by Django 3.2.6 on 2021-09-19 06:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kitchens', '0003_alter_kitchen_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=255),
        ),
    ]
