# Generated by Django 5.0.6 on 2024-08-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname_reg', models.CharField(max_length=255)),
                ('dob_reg', models.DateField()),
                ('age_reg', models.CharField(max_length=3)),
                ('email_reg', models.EmailField(max_length=255)),
                ('phono_reg', models.CharField(max_length=10, unique=True)),
                ('username_reg', models.CharField(max_length=255)),
                ('password_reg', models.CharField(max_length=255)),
                ('cpassword_reg', models.CharField(max_length=255)),
            ],
        ),
    ]
