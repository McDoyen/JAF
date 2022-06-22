# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

INPUT_TYPES = (('text', 'text'), ('date', 'date'))


class PersonalInformation(models.Model):
    INPUT_TYPES = (('text', 'text'), ('date', 'date'), ('email', 'email'),
                   ('file', 'file'), ('image', 'image'), ('number', 'number'), ('tel', 'tel'))
    question_text = models.CharField(max_length=200)
    question_index = models.IntegerField(default=0)
    input_type = models.CharField(
        default='text', max_length=6, choices=INPUT_TYPES)

    def __str__(self):
        return self.question_text


class AcademicQualification(models.Model):
    title = models.CharField(max_length=200)
    title_index = models.IntegerField(default=0)
    input_type = models.CharField(
        default='text', max_length=6, choices=INPUT_TYPES)

    def __str__(self):
        return self.title


class WorkingExperience(models.Model):
    title = models.CharField(max_length=200)
    title_index = models.IntegerField(default=0)
    input_type = models.CharField(
        default='text', max_length=6, choices=INPUT_TYPES)

    def __str__(self):
        return self.title


class Reference(models.Model):
    INPUT_TYPES = (('text', 'text'), ('tel', 'tel'), ('email', 'email'))

    title = models.CharField(max_length=200)
    title_index = models.IntegerField(default=0)
    input_type = models.CharField(
        default='text', max_length=6, choices=INPUT_TYPES)

    def __str__(self):
        return self.title
