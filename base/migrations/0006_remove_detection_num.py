# Generated by Django 4.0.1 on 2023-03-25 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_detection_options_detection_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detection',
            name='num',
        ),
    ]
