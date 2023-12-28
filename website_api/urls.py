from django.contrib import admin
from django.urls import path
from website_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('about_institution/', views.AboutInstitutionList.as_view()),
    path('about_institution/<int:pk>/', views.AboutInstitutionDetailsList.as_view()),
    path('overview/', views.OverviewList.as_view()),
    path('overview/<int:pk>/', views.OverviewDetailsList.as_view()),
    path('course_details/', views.CourseDetailsList.as_view()),
    path('course_details/<int:pk>/', views.CourseDetailsDetailedList.as_view()),
    path('cost_funding/', views.CostFundingList.as_view()),
    path('cost_funding/<int:pk>/', views.CostFundingDetailedList.as_view()),
    path('online_learning/', views.OnlineProgramList.as_view()),
    path('online_learning/<int:pk>/', views.OnlineProgramDetailedList.as_view()),
    path('requirement/', views.RequirementList.as_view()),
    path('requirement/<int:pk>/', views.RequirementDetailedList.as_view()),
    path('service/', views.ServiceList.as_view()),
    path('service/<int:pk>/', views.ServiceDetailedList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
