# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('question_index')[:6]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'introduction/index.html', context)
