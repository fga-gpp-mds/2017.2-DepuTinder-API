# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_questionnaire_questionstotal'),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_questionnaire', to='questionnaire.Questionnaire'),
        ),
    ]
