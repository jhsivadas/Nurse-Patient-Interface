# Generated by Django 3.2 on 2021-05-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20210420_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]