# Generated by Django 3.2 on 2022-10-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_flight_datee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='datee',
            field=models.CharField(max_length=30),
        ),
    ]
