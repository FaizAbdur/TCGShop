# Generated by Django 4.2.4 on 2023-09-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
    ]