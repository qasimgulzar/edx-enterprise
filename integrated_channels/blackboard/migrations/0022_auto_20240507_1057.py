# Generated by Django 3.2.23 on 2024-05-07 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blackboard', '0021_auto_20240423_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blackboardenterprisecustomerconfiguration',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='blackboardenterprisecustomerconfiguration',
            name='client_secret',
        ),
    ]
