# Generated by Django 2.1 on 2019-02-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190227_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='attended',
            field=models.BooleanField(default=False),
        ),
    ]
