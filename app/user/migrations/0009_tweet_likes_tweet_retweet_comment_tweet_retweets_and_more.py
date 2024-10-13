# Generated by Django 5.1.1 on 2024-10-09 20:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0008_user_follower_count_user_following_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_tweets", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="tweet",
            name="retweet_comment",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="tweet",
            name="retweets",
            field=models.ManyToManyField(
                blank=True, related_name="retweeted_tweets", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="like",
            name="tweet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tweet_likes",
                to="user.tweet",
            ),
        ),
        migrations.AlterField(
            model_name="tweet",
            name="original_tweet",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="retweet_set",
                to="user.tweet",
            ),
        ),
    ]
