# Generated by Django 2.1.5 on 2019-08-28 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20180419_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='restaurants.Restaurant'),
        ),
    ]
