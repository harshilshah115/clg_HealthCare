# Generated by Django 5.0.6 on 2024-08-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCare', '0006_alter_register_image_reg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='image_reg',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]