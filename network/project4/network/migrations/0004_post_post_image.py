# Generated by Django 4.0.3 on 2022-03-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_alter_userprofile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='postImg'),
        ),
    ]
