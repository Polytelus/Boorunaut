# Generated by Django 2.1.2 on 2018-10-23 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booru', '0016_post_tags_mirror'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alias',
            name='approver',
        ),
        migrations.RemoveField(
            model_name='alias',
            name='author',
        ),
        migrations.RemoveField(
            model_name='alias',
            name='from_tag',
        ),
        migrations.RemoveField(
            model_name='alias',
            name='to_tag',
        ),
        migrations.DeleteModel(
            name='Alias',
        ),
    ]