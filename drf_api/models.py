from django.db import models
# Create your models here.
class Faculty(models.Model):
   name = models.CharField(max_length=100)
   mob_no = models.CharField(max_length=10)
   salary = models.IntegerField()

class CourceInfo(models.Model):
   name = models.CharField(max_length=100)
   duration = models.IntegerField()
   fees = models.IntegerField()

   
class Student(models.Model):
   name = models.CharField(max_length=100)
   birth_year = models.IntegerField()
   address = models.CharField(max_length=100)
   mob_no = models.CharField(max_length=10)
   course = models.ForeignKey(CourceInfo, on_delete=models.DO_NOTHING)


class Subject(models.Model):
   name = models.CharField(max_length=100)
   faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)
   






   




