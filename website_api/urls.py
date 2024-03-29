from django.contrib import admin
from django.urls import path
from website_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('universities/', views.UniversitiesList.as_view()),
    path('universities/<int:pk>/', views.UniversitiesDetailsList.as_view()),
    path('programs/', views.ProgramsList.as_view()),
    path('programs/<int:pk>/', views.ProgramsDetailsList.as_view()),
    path('overview/', views.OverviewList.as_view()),
    path('overview/<int:pk>/', views.OverviewDetailsList.as_view()),
    path('course_details/', views.CourseDetailsList.as_view()),
    path('course_details/<int:pk>/', views.CourseDetailsDetailedList.as_view()),
    path('cost_funding/', views.CostFundingList.as_view()),
    path('cost_funding/<int:pk>/', views.CostFundingDetailedList.as_view()),
    path('online_learning/', views.OnlineLearningList.as_view()),
    path('online_learning/<int:pk>/', views.OnlineLearningDetailedList.as_view()),
    path('requirement/', views.RequirementList.as_view()),
    path('requirement/<int:pk>/', views.RequirementDetailedList.as_view()),
    path('service/', views.ServiceList.as_view()),
    path('service/<int:pk>/', views.ServiceDetailedList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
