# Generated by Django 2.2.6 on 2019-11-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191102_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default=True, upload_to='post_image'),
        ),
    ]
