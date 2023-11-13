# Generated by Django 4.2.2 on 2023-07-04 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_generaladditionalinfo_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_education', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_work_experience', to=settings.AUTH_USER_MODEL),
        ),
    ]