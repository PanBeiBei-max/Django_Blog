# Generated by Django 2.2.3 on 2021-12-16 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time', 'name'], 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
    ]
