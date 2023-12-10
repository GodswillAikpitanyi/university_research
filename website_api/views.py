from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .serializers import AllProgramsSerializer, CourseDetailsSerializer, UniversitiesSerializer, CostFundingSerializer,\
    ELearningSerializer, ServiceSerializer, RequirementSerializer
from .models import AllPrograms, CourseDetails, Universities, CostFunding, ELearning, Service, Requirement


class UniversitiesList(APIView):
    """
    List all universities, or create a new university
    """

    def get(self, request, format=None):
        universities = Universities.objects.all()
        serializer = UniversitiesSerializer(universities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UniversitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UniversitiesDetailsList(APIView):
    """
    Retrieve , update or delete a university instance
    """

    def get_object(self, pk):
        try:
            return Universities.objects.get(pk=pk)
        except Universities.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        universities = self.get_object(pk)
        serializer = UniversitiesSerializer(universities)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        universities = self.get_object(pk)
        serializer = UniversitiesSerializer(universities, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        universities = self.get_object(pk)
        universities.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


