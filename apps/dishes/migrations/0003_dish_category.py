# Generated by Django 3.2.6 on 2021-08-31 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20210831_0848'),
        ('dishes', '0002_dish_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='menus.category'),
            preserve_default=False,
        ),
    ]
