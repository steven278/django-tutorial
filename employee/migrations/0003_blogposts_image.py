# Generated by Django 4.1 on 2022-10-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_blogposts'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogposts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
