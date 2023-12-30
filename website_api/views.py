
from rest_framework import generics

from .serializers import UniversitiesSerializer, OverviewSerializer, CourseDetailsSerializer, CostFundingSerializer, \
    RequirementSerializer, ServiceSerializer, OnlineLearningSerializer, ProgramsSerializer
from .models import Universities, Overview, CourseDetails, CostFunding, Requirement, Service, OnlineLearning, Programs



class UniversitiesList(generics.ListCreateAPIView):

    """
    List all programs, or create a new program
    """
    queryset = Universities.objects.all()
    serializer_class = UniversitiesSerializer


class UniversitiesDetailsList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all course details per program
    """
    queryset = Universities.objects.all()
    serializer_class = UniversitiesSerializer



class ProgramsList(generics.ListCreateAPIView):

    """
    List all programs, or create a new program
    """
    queryset = Programs.objects.all()
    serializer_class = ProgramsSerializer


class ProgramsDetailsList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all course details per program
    """
    queryset = Programs.objects.all()
    serializer_class = ProgramsSerializer


class OverviewList(generics.ListCreateAPIView):

    """
    List all programs, or create a new program
    """
    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer


class OverviewDetailsList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all course details per program
    """
    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer



class CourseDetailsList(generics.ListCreateAPIView):

    """
    List all programs, or create a new program
    """
    queryset = CourseDetails.objects.all()
    serializer_class = CourseDetailsSerializer


class CourseDetailsDetailedList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all course details per program
    """
    queryset = CourseDetails.objects.all()
    serializer_class = CourseDetailsSerializer


class CostFundingList(generics.ListCreateAPIView):

    """
    List all programs, or create a new program
    """
    queryset = CostFunding.objects.all()
    serializer_class = CostFundingSerializer


class CostFundingDetailedList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all course details per program
    """
    queryset = CostFunding.objects.all()
    serializer_class = CostFundingSerializer


class OnlineProgramList(generics.ListCreateAPIView):

    """
    List all programs, or create a new program
    """
    queryset = OnlineLearning.objects.all()
    serializer_class = OnlineLearningSerializer


class OnlineProgramDetailedList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all course details per program
    """
    queryset = OnlineLearning.objects.all()
    serializer_class = OnlineLearningSerializer


class ServiceList(generics.ListCreateAPIView):

    """
    List all programs, or create a new program
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetailedList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all course details per program
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class RequirementList(generics.ListCreateAPIView):
    """
    List all programs, or create a new program
    """
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class RequirementDetailedList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all course details per program
    """
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


