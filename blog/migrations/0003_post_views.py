# Generated by Django 2.1.5 on 2019-02-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190126_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
