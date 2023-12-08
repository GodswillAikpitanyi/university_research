from django.contrib import admin
from .models import (Users, Universities, AllPrograms, Service, Support, Requirement, AcademicRequirement,
                     LanguageRequirement, ApplicationDeadline, ELearning, CostFunding, CourseDetails, Organization,
                     AssessmentType, Supplementary, InternationalElement, SummerTopics, SummerOptionalTopics,
                     WinterTopics, WinterOptionalTopics, ThirdSemester)

admin.site.register([Users, Universities, Service, Support, Requirement, AcademicRequirement, LanguageRequirement,
                     ApplicationDeadline, ELearning, CostFunding, AllPrograms, CourseDetails, Organization,
                     AssessmentType, Supplementary, InternationalElement, SummerTopics, SummerOptionalTopics,
                     WinterTopics, WinterOptionalTopics, ThirdSemester])