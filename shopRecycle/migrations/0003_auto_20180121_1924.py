# Generated by Django 2.0.dev20170813003239 on 2018-01-21 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopRecycle', '0002_auto_20170924_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shopRecycle.Category'),
        ),
    ]
