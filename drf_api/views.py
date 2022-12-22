from django.shortcuts import render


from rest_framework import viewsets
from drf_api.serializers import CourceInfoSerializer, StudentSerializer,FacultySerializer,SubjectSerializer
from drf_api.models import CourceInfo, Faculty, Student,Subject



class StudentViewSet(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer


class CourceInfoViewSet(viewsets.ModelViewSet):
   queryset = CourceInfo.objects.all()
   serializer_class = CourceInfoSerializer


class FacultyViewSet(viewsets.ModelViewSet):
   queryset = Faculty.objects.all()
   serializer_class = FacultySerializer


class SubjectViewSet(viewsets.ModelViewSet):
   queryset = Subject.objects.all()
   serializer_class = SubjectSerializer

