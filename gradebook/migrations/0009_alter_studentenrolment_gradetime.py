# Generated by Django 4.0.4 on 2022-05-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook', '0008_alter_studentenrolment_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenrolment',
            name='gradeTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
