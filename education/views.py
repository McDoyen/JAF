# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import TableColomn


def index(request):
    latest_colomn_list = TableColomn.objects.order_by('title_index')[:50]
    context = {'latest_colomn_list': latest_colomn_list}
    return render(request, 'education/index.html', context)
