# Generated by Django 5.0.6 on 2024-09-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCare', '0018_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='app_status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
