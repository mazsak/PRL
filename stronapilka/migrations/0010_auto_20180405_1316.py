# Generated by Django 2.0.3 on 2018-04-05 13:16

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stronapilka', '0009_auto_20180405_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zespol',
            name='kraj',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]