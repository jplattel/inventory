# Generated by Django 2.2.6 on 2019-12-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='profile_image/default.png', upload_to='profile_image'),
        ),
    ]
