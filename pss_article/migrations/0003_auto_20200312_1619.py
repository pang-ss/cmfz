# Generated by Django 2.0.6 on 2020-03-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pss_article', '0002_pic_datatime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pic',
            name='datatime',
        ),
        migrations.AddField(
            model_name='pic',
            name='datetime',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
