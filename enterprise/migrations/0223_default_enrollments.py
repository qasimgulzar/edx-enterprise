# Generated by Django 4.2.15 on 2024-10-15 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprise', '0222_alter_enterprisegroup_group_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultEnterpriseEnrollmentIntention',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content_type', models.CharField(choices=[('course', 'Course'), ('course_run', 'Course Run')], help_text='The type of content (e.g. a course vs. a course run).', max_length=127)),
                ('content_key', models.CharField(help_text='A course or course run that related users should be automatically enrolled into.', max_length=255)),
                ('enterprise_customer', models.ForeignKey(help_text='The customer for which this default enrollment will be realized.', on_delete=django.db.models.deletion.CASCADE, related_name='default_enrollment_intentions', to='enterprise.enterprisecustomer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalDefaultEnterpriseEnrollmentRealization',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('intended_enrollment', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='enterprise.defaultenterpriseenrollmentintention')),
                ('realized_enrollment', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='enterprise.enterprisecourseenrollment')),
            ],
            options={
                'verbose_name': 'historical default enterprise enrollment realization',
                'verbose_name_plural': 'historical default enterprise enrollment realizations',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDefaultEnterpriseEnrollmentIntention',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('content_type', models.CharField(choices=[('course', 'Course'), ('course_run', 'Course Run')], help_text='The type of content (e.g. a course vs. a course run).', max_length=127)),
                ('content_key', models.CharField(help_text='A course or course run that related users should be automatically enrolled into.', max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('enterprise_customer', models.ForeignKey(blank=True, db_constraint=False, help_text='The customer for which this default enrollment will be realized.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='enterprise.enterprisecustomer')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical default enterprise enrollment intention',
                'verbose_name_plural': 'historical default enterprise enrollment intentions',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='DefaultEnterpriseEnrollmentRealization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('intended_enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.defaultenterpriseenrollmentintention')),
                ('realized_enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.enterprisecourseenrollment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='defaultenterpriseenrollmentintention',
            name='realized_enrollments',
            field=models.ManyToManyField(through='enterprise.DefaultEnterpriseEnrollmentRealization', to='enterprise.enterprisecourseenrollment'),
        ),
    ]