from django.contrib import admin
from .models import (Users, Universities, AllPrograms, Overview, CourseDetails, AssessmentType, InternationalElement,
                     CostFunding, Requirement, Service, OnlineProgram, OnlineLearning)

admin.site.register([Users, Universities, AllPrograms, Overview, CourseDetails, AssessmentType, InternationalElement,
                     CostFunding, Requirement, Service, OnlineProgram, OnlineLearning])
