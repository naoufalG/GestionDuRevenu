# Generated by Django 3.2 on 2021-04-20 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_enfant'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enfant',
            options={'verbose_name': 'Enfant'},
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='famille',
        ),
    ]
