# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_messageattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='msgid',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
