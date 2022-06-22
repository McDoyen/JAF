# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import PersonalInformation
from .models import AcademicQualification
from .models import WorkingExperience
from .models import Reference


def introduction(request):
    latest_question_list = PersonalInformation.objects.order_by('question_index')[
        :50]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'forms/index.html', context)


def education(request):
    latest_colomn_list = AcademicQualification.objects.values(
        'title', 'input_type').order_by('title_index')
    input_type_query_set = AcademicQualification.objects.values_list(
        'input_type', flat=True)
    context = {'latest_colomn_list': list(
        latest_colomn_list), "input_type_query_set": list(input_type_query_set)}
    return render(request, 'forms/education.html', context)


def work(request):
    latest_colomn_list = WorkingExperience.objects.values(
        'title', 'input_type').order_by('title_index')
    input_type_query_set = WorkingExperience.objects.values_list(
        'input_type', flat=True)
    context = {'latest_colomn_list': list(
        latest_colomn_list), "input_type_query_set": list(input_type_query_set)}
    return render(request, 'forms/work.html', context)


def reference(request):
    latest_colomn_list = Reference.objects.values(
        'title', 'input_type').order_by('title_index')
    input_type_query_set = Reference.objects.values_list(
        'input_type', flat=True)
    context = {'latest_colomn_list': list(
        latest_colomn_list), "input_type_query_set": list(input_type_query_set)}
    return render(request, 'forms/reference.html', context)
