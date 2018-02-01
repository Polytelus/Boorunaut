# Generated by Django 2.0 on 2018-01-05 16:19

import booru.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=100)),
                ('title_singular', models.CharField(blank=True, max_length=100)),
                ('title_plural', models.CharField(blank=True, max_length=100)),
                ('color', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.ImageField(blank=True, upload_to=booru.models.get_file_path_preview)),
                ('sample', models.ImageField(blank=True, upload_to=booru.models.get_file_path_sample)),
                ('image', models.ImageField(blank=True, upload_to=booru.models.get_file_path_image)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('source', models.URLField(blank=True)),
                ('score', models.IntegerField(default=0)),
                ('favorites', models.IntegerField(default=0)),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('locked', models.BooleanField(default=False)),
                ('rating', models.IntegerField(choices=[(0, 'None'), (1, 'Safe'), (2, 'Questionable'), (3, 'Explicit')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Deleted')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TaggedPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(db_index=True, max_length=50, verbose_name='Object id')),
                ('label', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=2500)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booru.Category')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booru_taggedpost_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booru_taggedpost_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='posts', through='booru.TaggedPost', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='post',
            name='uploader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
