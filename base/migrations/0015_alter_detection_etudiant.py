# Generated by Django 3.2.16 on 2023-03-31 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_detection_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='etudiant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.roommember'),
        ),
    ]
