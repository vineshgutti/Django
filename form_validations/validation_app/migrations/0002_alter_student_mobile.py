# Generated by Django 4.1.7 on 2023-03-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
