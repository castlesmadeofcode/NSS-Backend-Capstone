# Generated by Django 3.0.7 on 2020-06-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstoneapp', '0002_auto_20200616_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='image',
            field=models.CharField(max_length=75, null=True),
        ),
    ]
