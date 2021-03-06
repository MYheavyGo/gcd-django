# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-04 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('stddata', '0002_initial_data'),
        ('gcd', '0016_delete_creatoraward'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('sort_name', models.CharField(db_index=True, max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('year_created', models.IntegerField(db_index=True, null=True)),
                ('year_created_uncertain', models.BooleanField(default=False)),
                ('notes', models.TextField()),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'gcd_feature',
            },
        ),
        migrations.CreateModel(
            name='FeatureLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('sort_name', models.CharField(db_index=True, max_length=255)),
                ('year_began', models.IntegerField(db_index=True, null=True)),
                ('year_ended', models.IntegerField(null=True)),
                ('year_began_uncertain', models.BooleanField(default=False)),
                ('year_ended_uncertain', models.BooleanField(default=False)),
                ('notes', models.TextField()),
                ('feature', models.ManyToManyField(db_table=b'gcd_feature_logo_2_feature', to='gcd.Feature')),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'gcd_feature_logo',
                'verbose_name_plural': 'Feature Logos',
            },
        ),
        migrations.CreateModel(
            name='FeatureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'gcd_feature_type',
            },
        ),
        migrations.AddField(
            model_name='feature',
            name='feature_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gcd.FeatureType'),
        ),
        migrations.AddField(
            model_name='feature',
            name='keywords',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='feature',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stddata.Language'),
        ),
    ]
