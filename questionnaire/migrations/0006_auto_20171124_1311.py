# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_remove_question_questionnaire'),
        ('questionnaire', '0005_auto_20171124_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='questions',
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='questions',
            field=models.ManyToManyField(to='question.Question'),
        ),
    ]