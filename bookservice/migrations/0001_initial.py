# Generated by Django 3.2 on 2022-06-13 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id',
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('date',
                 models.DateField()),
                ('service_type',
                 models.CharField(
                     choices=[
                         ('Bike fit',
                          'Bike fit'),
                         ('Repair',
                          'Repair'),
                         ('Full service',
                          'Full service')],
                     default='Repair',
                     max_length=40)),
                ('bike_type',
                 models.CharField(
                     choices=[
                         ('Hybrid',
                          'Hybrid'),
                         ('Road',
                          'Road')],
                     default='Hybrid',
                     max_length=15)),
                ('user_profile',
                 models.ForeignKey(
                     blank=True,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='bookings',
                     to='profiles.userprofile')),
            ],
        ),
    ]
