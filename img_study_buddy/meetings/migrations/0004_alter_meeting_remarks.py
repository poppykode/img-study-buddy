# Generated by Django 4.2.2 on 2023-07-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_rename_remarks_meeting_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
