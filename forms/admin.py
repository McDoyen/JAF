# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import PersonalInformation
from .models import AcademicQualification
from .models import WorkingExperience
from .models import Reference

admin.site.register(PersonalInformation)
admin.site.register(AcademicQualification)
admin.site.register(WorkingExperience)
admin.site.register(Reference)
