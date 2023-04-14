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


class Counts(models.Model):
    user = models.TextField(default=None)
    
    def __str__(self):
        return self.user
