# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 08:20
from __future__ import unicode_literals

from django.db import models, migrations

class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0021_add_wg_states'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newrevisiondocevent',
            old_name='rev',
            new_name='revision',
        ),
        migrations.RenameField(
            model_name='submissiondocevent',
            old_name='rev',
            new_name='revision',
        ),
        migrations.AddField(
            model_name='docevent',
            name='rev',
            field=models.CharField(blank=True, max_length=16, verbose_name=b'revision'),
        ),
    ]
