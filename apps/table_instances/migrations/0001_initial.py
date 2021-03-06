# Generated by Django 3.2.6 on 2021-09-01 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=255)),
                ('is_valid', models.BooleanField(default=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='tables.table')),
            ],
        ),
    ]
