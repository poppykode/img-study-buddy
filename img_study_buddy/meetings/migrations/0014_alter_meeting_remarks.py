# Generated by Django 4.2.2 on 2023-10-16 08:26

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0013_meeting_was_meeting_rejected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='remarks',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
