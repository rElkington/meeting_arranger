# Generated by Django 2.1 on 2019-01-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190106_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='lect_name',
        ),
        migrations.AddField(
            model_name='meeting',
            name='lect_name',
            field=models.ManyToManyField(to='posts.staff_users'),
        ),
    ]