from django.db import models


# Create your models here.

class schooldetails(models.Model):
    scname = models.CharField(max_length=100)
    sctrusty = models.CharField(max_length=50)
    scprincipal = models.CharField(max_length=50)
    studentcapacity = models.IntegerField()
    schooladd = models.TextField()

    def __str__(self):
        return self.scname



class Student(models.Model):
    sname = models.CharField(max_length=100)
    sroll = models.IntegerField()
    sgender = models.CharField(max_length=100)
    sstandard = models.IntegerField()
    ssubject = models.TextField()
    scity = models.CharField(max_length=50)
    sjoindate = models.CharField(max_length=50, null=True, blank=True)
    scid = models.ForeignKey(schooldetails,blank=True,null=True,on_delete=models.CASCADE,to_field='id')


    def __str__(self):
        return self.sname

class StdPresent(models.Model):
    stdroll = models.IntegerField()
    stdstandard = models.IntegerField()
    stdspresent = models.CharField(max_length=20)
    stddate = models.DateField()

    def __str__(self):
        return self.stdname