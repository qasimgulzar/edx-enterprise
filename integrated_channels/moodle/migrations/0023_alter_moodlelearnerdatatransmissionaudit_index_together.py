# Generated by Django 3.2.15 on 2023-01-03 14:48

from django.db import connection, migrations


def generate_index_sql(db_engine):
    if 'mysql' in db_engine:
        return """
            CREATE INDEX moodle_mldta_85936b55_idx
            ON moodle_moodlelearnerdatatransmissionaudit (enterprise_customer_uuid, plugin_configuration_id)
            ALGORITHM=INPLACE LOCK=NONE
        """
    elif 'postgresql' in db_engine:
        return """
            CREATE INDEX moodle_mldta_85936b55_idx
            ON moodle_moodlelearnerdatatransmissionaudit (enterprise_customer_uuid, plugin_configuration_id)
        """
    else:
        raise ValueError("Unsupported database engine")


def drop_index_sql(db_engine):
    return """
        DROP INDEX moodle_mldta_85936b55_idx
        ON moodle_moodlelearnerdatatransmissionaudit
    """


class Migration(migrations.Migration):
    dependencies = [
        ('moodle', '0022_auto_20221220_1527'),
    ]

    # Determine the database engine
    db_engine = connection.settings_dict['ENGINE']

    operations = []

    if 'sqlite3' in db_engine:
        operations.append(
            migrations.AlterIndexTogether(
                name='moodlelearnerdatatransmissionaudit',
                index_together={('enterprise_customer_uuid', 'plugin_configuration_id')},
            )
        )
    else:
        operations.append(
            migrations.SeparateDatabaseAndState(
                state_operations=[
                    migrations.AlterIndexTogether(
                        name='moodlelearnerdatatransmissionaudit',
                        index_together={('enterprise_customer_uuid', 'plugin_configuration_id')},
                    ),
                ],
                database_operations=[
                    # Adjust SQL for MySQL and PostgreSQL
                    migrations.RunSQL(
                        sql=generate_index_sql(db_engine),
                        reverse_sql=drop_index_sql(db_engine),
                    ),
                ]
            )
        )
