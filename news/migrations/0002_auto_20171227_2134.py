# Generated by Django 2.0.dev20170813003239 on 2017-12-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='text',
            field=models.TextField(),
        ),
    ]