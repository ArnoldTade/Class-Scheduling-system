# Generated by Django 4.2.1 on 2024-02-19 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_sched', '0022_alter_classschedule_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classschedule',
            name='end_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='classschedule',
            name='start_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='classschedule',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]
