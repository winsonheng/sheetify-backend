# Generated by Django 4.1.9 on 2023-07-20 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 20, 14, 1, 21, 506834, tzinfo=datetime.timezone.utc)),
        ),
    ]
