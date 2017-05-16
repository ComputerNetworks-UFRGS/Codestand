# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 02:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0019_auto_20161207_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dochistory',
            name='title',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Please enter a string without control characters.', regex='^[^\x00-\x1f]*$')]),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Please enter a string without control characters.', regex='^[^\x00-\x1f]*$')]),
        ),
    ]