# Generated by Django 3.2.4 on 2021-07-08 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210708_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatesmodel',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
