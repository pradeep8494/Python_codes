from django.db import models


#   StudentInformation Model -
class StudentInfo(models.Model):
    RoleNo  =   models.CharField(primary_key = True, max_length=15)
    Name    =   models.CharField(max_length=120)
    Class   =   models.CharField(max_length=120)
    Mobile  =   models.CharField(max_length=15)
    Address =   models.TextField(blank=True)


#   StudentAcademics model - 
class StudentAcademics(models.Model):
    RoleNo      =   models.ForeignKey(to=StudentInfo, on_delete=models.CASCADE)
    Maths       =   models.IntegerField()
    Physics     =   models.IntegerField()
    Chemistry   =   models.IntegerField()
    Biology     =   models.IntegerField()
    English     =   models.IntegerField()
