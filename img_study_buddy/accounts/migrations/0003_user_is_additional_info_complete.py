# Generated by Django 4.2.2 on 2023-06-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_coach_user_time_zone_alter_user_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_additional_info_complete',
            field=models.BooleanField(default=False),
        ),
    ]
