# Generated by Django 4.2.15 on 2024-08-26 13:57

from django.db import migrations


def populate_decrypted_client_id_and_secret(apps, schema_editor):  # pragma: no cover
    """
    Populate the decrypted_client_id and decrypted_client_secret fields for all 
    existing CanvasEnterpriseCustomerConfiguration
    """
    CanvasEnterpriseCustomerConfiguration = apps.get_model('canvas', 'CanvasEnterpriseCustomerConfiguration')
    for config in CanvasEnterpriseCustomerConfiguration.objects.all():
        config.decrypted_client_id = config.client_id
        config.decrypted_client_secret = config.client_secret
        config.save()


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0036_canvasenterprisecustomerconfiguration_decrypted_client_id_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_decrypted_client_id_and_secret, reverse_code=migrations.RunPython.noop),
    ]
