# Generated by Django 4.2.2 on 2023-07-24 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_remove_meeting_station'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='Remarks',
            new_name='remarks',
        ),
    ]
