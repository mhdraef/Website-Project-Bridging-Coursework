# Generated by Django 3.0.6 on 2020-06-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200607_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bg',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]