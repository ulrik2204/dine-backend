# Generated by Django 3.1.6 on 2021-03-23 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dine_backend', '0004_auto_20210316_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinner',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='about_me',
            field=models.TextField(blank=True, default=''),
        ),
    ]
