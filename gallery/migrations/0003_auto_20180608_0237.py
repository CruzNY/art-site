# Generated by Django 2.0.6 on 2018-06-08 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_artwork_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='title',
            field=models.CharField(default='Title', max_length=25),
        ),
    ]
