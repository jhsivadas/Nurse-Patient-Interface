# Generated by Django 3.2 on 2021-07-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20210718_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]