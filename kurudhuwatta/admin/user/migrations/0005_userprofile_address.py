# Generated by Django 5.0.7 on 2024-07-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userprofile_delete_useregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
