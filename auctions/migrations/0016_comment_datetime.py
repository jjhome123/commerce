# Generated by Django 4.1.7 on 2023-03-25 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_remove_listing_comments_comment_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]