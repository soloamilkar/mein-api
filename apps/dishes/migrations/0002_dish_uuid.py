# Generated by Django 3.2.6 on 2021-08-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='uuid',
            field=models.CharField(default='asdg4ggdf54a5s4f5a4sg4', max_length=255),
            preserve_default=False,
        ),
    ]