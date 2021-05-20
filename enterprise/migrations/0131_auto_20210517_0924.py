# Generated by Django 2.2.19 on 2021-05-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0130_lms_customer_lp_search_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomer',
            name='reply_to',
            field=models.EmailField(blank=True, help_text="The email address where learner's reply to enterprise emails will be delivered.", max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomer',
            name='reply_to',
            field=models.EmailField(blank=True, help_text="The email address where learner's reply to enterprise emails will be delivered.", max_length=254, null=True),
        ),
    ]