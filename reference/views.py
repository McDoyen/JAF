# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from .models import TableColomn


def index(request):
    latest_colomn_list = TableColomn.objects.values(
        'title', 'input_type').order_by('title_index')
    input_type_query_set = TableColomn.objects.values_list(
        'input_type', flat=True)
    context = {'latest_colomn_list': list(
        latest_colomn_list), "input_type_query_set": list(input_type_query_set)}
    return render(request, 'reference/index.html', context)
