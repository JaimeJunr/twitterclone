# Generated by Django 5.1.1 on 2024-10-10 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0012_remove_tweet_retweet_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="retweet_content",
            field=models.TextField(blank=True, max_length=280),
        ),
    ]
