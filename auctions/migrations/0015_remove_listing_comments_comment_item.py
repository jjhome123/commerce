# Generated by Django 4.1.7 on 2023-03-25 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_comment_listing_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='item',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
    ]
