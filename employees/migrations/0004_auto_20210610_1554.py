# Generated by Django 3.1.12 on 2021-06-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20210610_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_no',
            field=models.IntegerField(unique=True),
        ),
    ]
