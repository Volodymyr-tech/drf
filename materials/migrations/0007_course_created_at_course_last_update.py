# Generated by Django 5.1.6 on 2025-04-07 21:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0006_alter_course_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='last_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
