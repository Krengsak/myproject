# Generated by Django 5.1.3 on 2025-02-08 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_hire_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='HireforAdmin',
            fields=[
                ('HireA_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Width', models.FloatField(verbose_name='Width (m.)')),
                ('Length', models.FloatField(verbose_name='Length (m.)')),
                ('Height', models.FloatField(verbose_name='Height (m.)')),
                ('Type', models.CharField(max_length=100)),
                ('Budget', models.CharField(max_length=150)),
                ('Location', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='hire',
            name='Budget',
            field=models.FloatField(max_length=150),
        ),
        migrations.AlterField(
            model_name='hire',
            name='Status',
            field=models.CharField(choices=[('in_progress', 'อยู่ระหว่างการทำ'), ('completed', 'ทำเสร็จสิ้นแล้ว'), ('waiting_confirmation', 'รอการยืนยัน')], default='waiting_confirmation', max_length=20, verbose_name='Status'),
        ),
        migrations.CreateModel(
            name='PredictHire',
            fields=[
                ('Predict_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Width', models.FloatField()),
                ('Length', models.FloatField()),
                ('Height', models.FloatField()),
                ('Type', models.CharField(max_length=100)),
                ('Budget', models.CharField(max_length=150)),
                ('Area', models.FloatField(verbose_name='Area')),
                ('Wood', models.IntegerField(verbose_name='Wood (pc.)')),
                ('Lighting', models.IntegerField(verbose_name='Lighting (pc.)')),
                ('Nail', models.IntegerField(verbose_name='Nail (box.)')),
                ('Table', models.IntegerField(verbose_name='Table')),
                ('Chair', models.IntegerField(verbose_name='Chair')),
                ('HireC_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.hire')),
            ],
        ),
    ]
