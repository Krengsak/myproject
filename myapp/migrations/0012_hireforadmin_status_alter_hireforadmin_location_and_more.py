# Generated by Django 5.1.3 on 2025-02-10 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_predicthire_hirea_id_alter_hire_budget_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hireforadmin',
            name='Status',
            field=models.CharField(choices=[('in_progress', 'อยู่ระหว่างการทำ'), ('completed', 'ทำเสร็จสิ้นแล้ว'), ('waiting_confirmation', 'รอการยืนยัน')], default='waiting_confirmation', max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='hireforadmin',
            name='Location',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='Chair',
            field=models.IntegerField(default=0, null=True, verbose_name='Chair Actual'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='Lighting',
            field=models.IntegerField(default=0, null=True, verbose_name='Lighting (pc.) Actual'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='Nail',
            field=models.IntegerField(default=0, null=True, verbose_name='Nail (box.) Actual'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='Table',
            field=models.IntegerField(default=0, null=True, verbose_name='Table Actual'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='Wood',
            field=models.IntegerField(default=0, null=True, verbose_name='Wood (pc.) Actual'),
        ),
    ]
