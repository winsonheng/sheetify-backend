# Generated by Django 4.1.9 on 2023-07-21 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_alter_song_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 21, 10, 31, 41, 480920, tzinfo=datetime.timezone.utc)),
        ),
    ]
