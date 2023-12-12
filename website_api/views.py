
from rest_framework import generics

from .serializers import AllProgramsSerializer, CourseDetailsSerializer, UniversitiesSerializer, CostFundingSerializer,\
    ELearningSerializer, ServiceSerializer, RequirementSerializer
from .models import AllPrograms, CourseDetails, Universities, CostFunding, ELearning, Service, Requirement





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


class AllProgramsList(generics.ListCreateAPIView):

    """
    List all programs, or create a new program
    """
    queryset = AllPrograms.objects.all()
    serializer_class = AllProgramsSerializer


class AllProgramsDetailsList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all course details per program
    """
    queryset = AllPrograms.objects.all()
    serializer_class = AllProgramsSerializer



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


class ELearningList(generics.ListCreateAPIView):

    """
    List all programs, or create a new program
    """
    queryset = ELearning.objects.all()
    serializer_class = ELearningSerializer


class ELearningDetailedList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all course details per program
    """
    queryset = ELearning.objects.all()
    serializer_class = ELearningSerializer


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


