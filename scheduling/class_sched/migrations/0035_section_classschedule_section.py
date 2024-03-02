# Generated by Django 4.2.1 on 2024-03-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_sched', '0034_week_remove_classschedule_days_of_week_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=100)),
                ('yr_level', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='classschedule',
            name='section',
            field=models.ManyToManyField(to='class_sched.section'),
        ),
    ]