# Generated by Django 4.2.5 on 2023-10-02 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_id_alter_custombloguser_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(default=datetime.datetime(2023, 10, 2, 16, 21, 49, 23079, tzinfo=datetime.timezone.utc), max_length=500),
            preserve_default=False,
        ),
    ]
