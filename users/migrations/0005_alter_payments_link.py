# Generated by Django 5.1.6 on 2025-03-31 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_payments_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
