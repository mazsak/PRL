# Generated by Django 2.0.3 on 2018-04-05 13:53

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stronapilka', '0010_auto_20180405_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liga',
            name='kraj',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='stadion',
            name='kraj',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='zawodnik',
            name='kraj',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
