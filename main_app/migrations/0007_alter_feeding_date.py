# Generated by Django 4.2.2 on 2023-06-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_feeding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(),
        ),
    ]