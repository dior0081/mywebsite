# Generated by Django 4.1.5 on 2023-01-13 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mydjango", "0003_alter_posting_poster"),
    ]

    operations = [
        migrations.AddField(
            model_name="posting",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 1, 13, 12, 0, 20, 374158, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="posting",
            name="time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 1, 13, 12, 0, 34, 208987, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Время",
            ),
            preserve_default=False,
        ),
    ]
