# Generated by Django 3.2.4 on 2021-07-02 13:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 2, 13, 46, 48, 509739, tzinfo=utc)),
        ),
    ]
