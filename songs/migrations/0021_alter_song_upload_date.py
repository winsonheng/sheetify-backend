# Generated by Django 4.1.9 on 2023-06-29 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0020_alter_song_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 29, 15, 40, 55, 951930, tzinfo=datetime.timezone.utc)),
        ),
    ]
