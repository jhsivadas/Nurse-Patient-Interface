# Generated by Django 3.2 on 2021-04-16 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_pain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pain',
            name='name',
        ),
    ]