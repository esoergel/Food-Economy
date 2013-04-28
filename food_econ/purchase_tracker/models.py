from django.db import models
from django.contrib.auth.models import User


class BusinessCategory(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    coords = models.CharField('GPS coordinates', max_length=50, blank=True)
    category = models.ForeignKey(BusinessCategory)

    def __unicode__(self):
        return self.name


# class Transport(models.Model):
#     name = models.CharField(max_length=50, blank=True)
    
#     def __unicode__(self):
#         return self.name

# class FoodCategory(models.Model):


class Motivation(models.Model):
    '''
    reason for purchasing at this location
    '''
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


# class Transport(models.Model):
#     name = models.CharField(max_length=50, blank=True)
    
#     def __unicode__(self):
#         return self.name


class Purchase(models.Model):
    user = models.ForeignKey(User)
    business = models.ForeignKey(Business)
    expenditure = models.DecimalField("Amount Spent", max_digits=6, decimal_places=2, blank=True)
    # transport = models.ForeignKey(Transport, blank=True)
    date = models.DateField(auto_now_add=True)
    reasons = models.ManyToManyField(Motivation)

    def __unicode__(self):
        return "%s at %s" % (self.user, self.business)

