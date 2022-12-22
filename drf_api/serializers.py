from rest_framework import serializers
from drf_api.models import CourceInfo, Faculty,Student, Subject

class StudentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Student
       fields = ('name','birth_year', 'address', 'mob_no','course')


class CourceInfoSerializer(serializers.ModelSerializer):
   class Meta:
       model = CourceInfo
       fields = ('name', 'duration','fees')


class FacultySerializer(serializers.ModelSerializer):
   class Meta:
       model = Faculty
       fields = ('name','mob_no', 'salary')

class SubjectSerializer(serializers.ModelSerializer):
   class Meta:
       model = Subject
       fields = ('name', 'faculty')







