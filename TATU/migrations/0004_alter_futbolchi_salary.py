# Generated by Django 3.2.5 on 2021-08-13 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TATU', '0003_futbolchi_klub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futbolchi',
            name='salary',
            field=models.DateTimeField(default=100),
        ),
    ]