# Generated by Django 4.2.5 on 2023-10-22 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_category_subscribers_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postCategory',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='categoryThrough',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='postThrough',
            new_name='post',
        ),
    ]
