# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TableColomn(models.Model):
    INPUT_TYPES = (('tel', 'tel'),
                   ('text', 'text'), ('email', 'email'))

    title = models.CharField(max_length=200)
    title_index = models.IntegerField(default=0)
    input_type = models.CharField(
        default='text', max_length=6, choices=INPUT_TYPES)

    def __str__(self):
        return self.title
