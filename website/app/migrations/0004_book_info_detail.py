# Generated by Django 2.1.2 on 2018-11-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book_info_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_info',
            name='detail',
            field=models.CharField(default='', max_length=10),
        ),
    ]
