from django.db import models

# Create your models here.


class SchemeList(models.Model):
    state = models.CharField(max_length=150)
    disabilityType = models.CharField(max_length=150)
    schemeName = models.TextField(max_length=100000)
    benefitCriteria = models.CharField(max_length=150)
    typesOfBenefit = models.CharField(max_length=150)

    def __str__(self):
        return self.typesOfBenefit


class VisitCounts(models.Model):
    user_ip = models.TextField(default=None)
    
    def __str__(self):
        return self.user

class FilterCounts(models.Model):
    user_ip = models.TextField(default=None)
    username = models.CharField(max_length=150, default=None)
    userage = models.CharField(max_length=10, default=None)
    
    def __str__(self):
        return self.user