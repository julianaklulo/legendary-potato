from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)


class Sport(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)
    price = models.FloatField()

class Customer(models.Model):
    name = models.CharField(max_length=100)
    num_doc = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True)
