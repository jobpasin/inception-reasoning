# Generated by Django 3.0.3 on 2020-04-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0003_auto_20200419_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
