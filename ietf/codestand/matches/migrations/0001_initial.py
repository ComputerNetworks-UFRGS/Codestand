# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('additional_information', models.CharField(max_length=255)),
                ('coder', models.IntegerField(null=True, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('reputation', models.IntegerField(null=True, blank=True)),
                ('is_archived', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DashboardConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.IntegerField(null=True, blank=True)),
                ('data', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Implementation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=50, choices=[(b'Twitter', b'Twitter'), (b'Facebook', b'Facebook'), (b'Jabber', b'Jabber'), (b'Mail', b'Email')])),
            ],
        ),
        migrations.CreateModel(
            name='ProjectContainer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.IntegerField(null=True, blank=True)),
                ('title', models.CharField(max_length=80)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('protocol', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('docs', models.CharField(max_length=10000, null=True, blank=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('code_request', models.ForeignKey(blank=True, to='requests.CodeRequest', null=True)),
                ('codings', models.ManyToManyField(to='matches.CodingProject')),
                ('contacts', models.ManyToManyField(to='matches.ProjectContact', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='projectcontainer',
            name='tags',
            field=models.ManyToManyField(to='matches.ProjectTag', blank=True),
        ),
        migrations.AddField(
            model_name='codingproject',
            name='contacts',
            field=models.ManyToManyField(to='matches.ProjectContact', blank=True),
        ),
        migrations.AddField(
            model_name='codingproject',
            name='links',
            field=models.ManyToManyField(to='matches.Implementation', blank=True),
        ),
        migrations.AddField(
            model_name='codingproject',
            name='tags',
            field=models.ManyToManyField(to='matches.ProjectTag', blank=True),
        ),
    ]
