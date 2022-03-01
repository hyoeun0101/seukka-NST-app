# Generated by Django 4.0.2 on 2022-03-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatars/sparta.png', upload_to='avatars'),
        ),
    ]