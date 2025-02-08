# Generated by Django 5.1.3 on 2025-01-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_hire_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='Status',
            field=models.CharField(choices=[('in_progress', 'อยู่ระหว่างการทำ'), ('completed', 'ทำเสร็จสิ้นแล้ว'), ('Waiting_confirmation', 'รอการยืนยัน')], default='Waiting_confirmation', max_length=20, verbose_name='สถานะ'),
        ),
    ]
