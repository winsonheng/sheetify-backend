# Generated by Django 4.1.9 on 2023-07-10 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0031_alter_song_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 10, 16, 1, 58, 436472, tzinfo=datetime.timezone.utc)),
        ),
    ]
