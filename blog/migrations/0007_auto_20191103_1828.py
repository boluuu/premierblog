# Generated by Django 2.2.6 on 2019-11-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191103_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(unique=True, upload_to='post_image'),
        ),
    ]
