# Generated by Django 5.0.6 on 2024-09-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCare', '0013_doctor_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_image',
            field=models.ImageField(blank=True, null=True, upload_to='doctor_image'),
        ),
    ]
