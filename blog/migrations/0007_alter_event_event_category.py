# Generated by Django 3.2 on 2022-06-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220614_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_category',
            field=models.CharField(choices=[('Ladies cycling', 'Ladies cycling'), ('Mens cycling', 'Mens cycling'), ('Racing', 'Racing'), ('Social', 'Social')], default='Racing', max_length=40),
        ),
    ]
