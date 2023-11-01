# Generated by Django 4.2.2 on 2023-10-14 12:15

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0004_offer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='offer',
            name='summary',
            field=tinymce.models.HTMLField(),
        ),
    ]
