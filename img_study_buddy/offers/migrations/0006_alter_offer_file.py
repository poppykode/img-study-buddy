# Generated by Django 4.2.2 on 2023-10-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_alter_offer_description_alter_offer_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]