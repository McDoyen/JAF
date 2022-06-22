# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class PersonalInformation(models.Model):
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


class AcademicQualification(models.Model):
    INPUT_TYPES = (('date', 'date'), ('text', 'text'))

    title = models.CharField(max_length=200)
    title_index = models.IntegerField(default=0)
    input_type = models.CharField(
        default='text', max_length=6, choices=INPUT_TYPES)

    def __str__(self):
        return self.title


class WorkingExperience(models.Model):
    INPUT_TYPES = (('text', 'text'), ('date', 'date'))

    title = models.CharField(max_length=200)
    title_index = models.IntegerField(default=0)
    input_type = models.CharField(
        default='text', max_length=6, choices=INPUT_TYPES)

    def __str__(self):
        return self.title


class Reference(models.Model):
    INPUT_TYPES = (('tel', 'tel'),
                   ('text', 'text'), ('email', 'email'))

    title = models.CharField(max_length=200)
    title_index = models.IntegerField(default=0)
    input_type = models.CharField(
        default='text', max_length=6, choices=INPUT_TYPES)

    def __str__(self):
        return self.title
