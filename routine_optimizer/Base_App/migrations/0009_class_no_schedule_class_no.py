# Generated by Django 5.1.6 on 2025-04-12 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0008_faculty_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='class_no',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='class_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Base_App.class_no'),
        ),
    ]
