# Generated by Django 4.2.1 on 2024-03-24 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_sched', '0005_alter_course_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classschedule',
            name='semester',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
