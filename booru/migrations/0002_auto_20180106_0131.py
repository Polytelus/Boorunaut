# Generated by Django 2.0 on 2018-01-06 03:31

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('booru', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='taggedpost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='taggedpost',
            name='description',
        ),
        migrations.RemoveField(
            model_name='taggedpost',
            name='label',
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='posts', through='booru.TaggedPost', to='booru.PostTag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='taggedpost',
            name='object_id',
            field=models.IntegerField(db_index=True, verbose_name='Object id'),
        ),
        migrations.AlterField(
            model_name='taggedpost',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booru_taggedpost_items', to='booru.PostTag'),
        ),
        migrations.AddField(
            model_name='posttag',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='booru.Category'),
        ),
    ]
