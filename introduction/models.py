# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    INPUT_TYPES = (
        ('date', 'date'), ('email', 'email'), ('file', 'file'), ('image',
                                                                 'image'), ('number', 'number'), ('tel', 'tel'), ('text', 'text')
    )
    question_text = models.CharField(max_length=200)
    question_index = models.IntegerField(default=0)
    input_type = models.CharField(
        default='text', max_length=6, choices=INPUT_TYPES)

    def __str__(self):
        return self.question_text
