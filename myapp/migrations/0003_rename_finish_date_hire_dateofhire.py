# Generated by Django 5.1.3 on 2024-12-31 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_hire'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hire',
            old_name='Finish_Date',
            new_name='Dateofhire',
        ),
    ]
