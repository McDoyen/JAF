# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import PersonalInformation
from .models import AcademicQualification
from .models import WorkingExperience
from .models import Reference


def getQuerySet(model, orderMethod):
    return model.objects.values().order_by(orderMethod)


def inputTypeQuerySet(model):
    return model.objects.values_list('input_type', flat=True)


def titleQuerySet(model):
    return model.objects.values_list('title', flat=True)


def context(model):
    return {'latest_column_list': list(
        getQuerySet(model, 'title_index')), 'input_type_query_set': list(inputTypeQuerySet(model)), 'title_query_set': list(titleQuerySet(model))}


def introduction(request):
    context = {'latest_question_list': getQuerySet(
        PersonalInformation, 'question_index')}
    return render(request, 'forms/index.html', context)


def education(request):
    return render(request, 'forms/education.html', context(AcademicQualification))


def work(request):
    return render(request, 'forms/work.html', context(WorkingExperience))


def reference(request):
    return render(request, 'forms/reference.html', context(Reference))
