# Generated by Django 4.2.2 on 2023-07-30 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0006_alter_meeting_was_meeting_attended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='requested_has_accepted',
        ),
    ]
