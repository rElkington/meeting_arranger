# Generated by Django 2.1 on 2019-01-02 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lect_name', models.CharField(max_length=200)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('descript', models.CharField(max_length=500)),
                ('attendance', models.BooleanField()),
                ('lecturer_details', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='staff_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='student_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='PostModel',
        ),
    ]
