# Generated by Django 4.2.5 on 2023-10-03 18:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featureImage',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='FeatureImage'),
        ),
    ]