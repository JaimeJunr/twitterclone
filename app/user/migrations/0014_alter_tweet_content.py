# Generated by Django 5.1.1 on 2024-10-10 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0013_tweet_retweet_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tweet",
            name="content",
            field=models.TextField(blank=True, max_length=280),
        ),
    ]
