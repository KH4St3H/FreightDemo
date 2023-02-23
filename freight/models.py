from django.db import models
from django.contrib.auth.models import AbstractUser, User


class CustomUser(AbstractUser):
    user = models.CharField(max_length=10, blank=True, null=True)
    password = None

    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=40)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ('name',)


class Factory(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class FreightCompany(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    associate_companies = models.ManyToManyField(Factory)


class Driver(models.Model):
    full_name = models.CharField(max_length=30)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Load(models.Model):
    declare_date = models.DateField()
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()

    class Status(models.TextChoices):
        HIDDEN = 'hidden', 'Not accepting'
        ACCEPTING = 'accepting', 'Accepting'
        COMPLETED = 'completed', 'Assigning completed'

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACCEPTING)
