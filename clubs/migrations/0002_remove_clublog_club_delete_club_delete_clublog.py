# Generated by Django 5.1 on 2024-08-28 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clublog',
            name='club',
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.DeleteModel(
            name='ClubLog',
        ),
    ]
