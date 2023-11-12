from django.contrib import admin
from .models import (Universities, AllPrograms, CourseDetails, Organization, AssessmentType, Supplementary,
                     InternationalElement, TopDetails, Summer, SummerOptional,
                     Winter, WinterOptional, ThirdSemester)

admin.site.register([Universities, AllPrograms, CourseDetails, Organization, AssessmentType, Supplementary,
                     InternationalElement, TopDetails, Summer, SummerOptional,
                     Winter, WinterOptional, ThirdSemester])
