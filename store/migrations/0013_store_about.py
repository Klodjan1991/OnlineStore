# Generated by Django 4.0.6 on 2022-08-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_store_abouttxt'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='about',
            field=models.TextField(default='-'),
        ),
    ]
