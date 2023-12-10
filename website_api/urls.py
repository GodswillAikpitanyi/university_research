from django.contrib import admin
from django.urls import path
from website_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('universities/', views.UniversitiesList.as_view()),
    path('universities/<int:pk>/', views.UniversitiesDetailsList.as_view()),
    path('all_programs/', views.AllProgramsList.as_view()),
    path('all_programs/<int:pk>/', views.AllProgramsDetailsList.as_view()),
    path('course_details/', views.CourseDetailsList.as_view()),
    path('course_details/<int:pk>/', views.CourseDetailsDetailedList.as_view()),
    path('cost_funding/', views.CostFundingList.as_view()),
    path('cost_funding/<int:pk>/', views.CostFundingDetailedList.as_view()),
    path('e_learning/', views.ELearningList.as_view()),
    path('e_learning/<int:pk>/', views.ELearningDetailedList.as_view()),
    path('requirement/', views.RequirementList.as_view()),
    path('requirement/<int:pk>/', views.RequirementDetailedList.as_view()),
    path('service/', views.ServiceList.as_view()),
    path('service/<int:pk>/', views.ServiceDetailedList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

