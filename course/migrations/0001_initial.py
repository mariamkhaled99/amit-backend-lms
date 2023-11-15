# Generated by Django 4.2.7 on 2023-11-14 22:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_description', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('course_credit_hours', models.IntegerField()),
                ('course_price', models.IntegerField()),
                ('certificate', models.TextField(blank=True, default='', null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='course')),
                ('rating', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]
