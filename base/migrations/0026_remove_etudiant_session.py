# Generated by Django 3.2.16 on 2023-04-13 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_auto_20230412_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='session',
        ),
    ]
