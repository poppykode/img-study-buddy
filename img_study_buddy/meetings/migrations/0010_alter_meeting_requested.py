# Generated by Django 4.2.2 on 2023-07-30 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meetings', '0009_alter_meeting_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='requested',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meeting_requested', to=settings.AUTH_USER_MODEL),
        ),
    ]
