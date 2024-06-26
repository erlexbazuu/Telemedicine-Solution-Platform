# Generated by Django 5.0.3 on 2024-04-28 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_prescription_file_appointments_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('denied', 'Denied')], default='pending', max_length=10)),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='home.appointments')),
            ],
        ),
        migrations.DeleteModel(
            name='AppointmentRequest',
        ),
    ]
