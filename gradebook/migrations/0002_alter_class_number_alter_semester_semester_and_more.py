# Generated by Django 4.0.3 on 2022-03-23 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='number',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='semester',
            name='year',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='studentenrollment',
            name='grade',
            field=models.IntegerField(max_length=3),
        ),
    ]