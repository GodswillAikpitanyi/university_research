from django.contrib import admin
from django.urls import path
from website_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('api/universities/', views.UniversitiesList.as_view()),
    path('api/universities/<int:pk>/', views.UniversitiesDetailsList.as_view()),
    path('api/all_programs/', views.AllProgramsList.as_view()),
    path('api/all_programs/<int:pk>/', views.AllProgramsDetailsList.as_view()),
    path('api/course_details/', views.CourseDetailsList.as_view()),
    path('api/course_details/<int:pk>/', views.CourseDetailsDetailedList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

