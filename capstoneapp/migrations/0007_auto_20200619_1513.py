# Generated by Django 3.0.7 on 2020-06-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstoneapp', '0006_auto_20200619_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
