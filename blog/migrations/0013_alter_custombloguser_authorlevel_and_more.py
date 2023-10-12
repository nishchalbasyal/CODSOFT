# Generated by Django 4.2.5 on 2023-10-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_custombloguser_authorlevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custombloguser',
            name='authorLevel',
            field=models.IntegerField(choices=[(2, 'Level 2 Author'), (3, 'Level 3 Author'), (1, 'Level 1 Author')], default=1),
        ),
        migrations.AlterField(
            model_name='custombloguser',
            name='bio',
            field=models.TextField(max_length=350),
        ),
    ]