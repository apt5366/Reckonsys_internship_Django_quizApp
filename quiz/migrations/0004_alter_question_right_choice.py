# Generated by Django 3.2.6 on 2021-08-17 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20210816_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='right_choice',
            field=models.IntegerField(default=1),
        ),
    ]
