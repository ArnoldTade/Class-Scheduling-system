# Generated by Django 4.2.1 on 2024-03-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_sched', '0036_alter_section_yr_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='section_college',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
