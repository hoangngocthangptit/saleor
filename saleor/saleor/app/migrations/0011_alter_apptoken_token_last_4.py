# Generated by Django 3.2.12 on 2022-03-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_update_app_tokens"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apptoken",
            name="token_last_4",
            field=models.CharField(max_length=4),
        ),
    ]
