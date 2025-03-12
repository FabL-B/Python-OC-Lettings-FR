# Generated by Django 3.0 on 2025-03-12 13:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
         migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Address',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                        ('street', models.CharField(max_length=64)),
                        ('city', models.CharField(max_length=64)),
                        ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                        ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                        ('country_iso_code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
                    ],
                    options={
                        'verbose_name_plural': 'Addresses',
                    },
                ),
            ],
            database_operations=[],
         ),
     ]
