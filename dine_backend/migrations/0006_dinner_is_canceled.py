# Generated by Django 3.1.6 on 2021-03-31 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dine_backend', '0005_auto_20210324_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinner',
            name='is_canceled',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
