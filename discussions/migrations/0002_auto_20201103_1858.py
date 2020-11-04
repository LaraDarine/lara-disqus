# Generated by Django 3.1.2 on 2020-11-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='image',
            new_name='demo_image',
        ),
        migrations.AddField(
            model_name='discussion',
            name='main_image',
            field=models.ImageField(default='discussions/discussion.png', upload_to='discussions/'),
        ),
    ]