# Generated by Django 4.0.3 on 2022-03-23 04:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook', '0002_alter_class_number_alter_semester_semester_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='semester',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='studentenrollment',
            name='grade',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
