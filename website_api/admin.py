from django.contrib import admin
from .models import (Users, Universities, Programs, Overview, CourseDetails, AssessmentType, InternationalElement,
                     CostFunding, Requirement, Service, OnlineLearning, OnlineLearningElement)

admin.site.register([Users, Universities, Programs, Overview, CourseDetails, AssessmentType, InternationalElement,
                     CostFunding, Requirement, Service, OnlineLearning, OnlineLearningElement])
