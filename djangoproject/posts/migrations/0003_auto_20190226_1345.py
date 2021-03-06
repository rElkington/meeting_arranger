# Generated by Django 2.1 on 2019-02-26 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_meeting_attended'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='student_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.student_users'),
        ),
        migrations.AddField(
            model_name='student_users',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
