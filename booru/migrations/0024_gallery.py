# Generated by Django 2.1.2 on 2018-10-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booru', '0023_auto_20181027_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
                ('posts', models.ManyToManyField(to='booru.Post')),
            ],
        ),
    ]