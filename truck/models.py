from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=40)
    mob_no = models.BigIntegerField(null=True, blank=True)
    driving_lisc = models.CharField(max_length=40, null=True, blank=True)
    no_of_vehicles = models.SmallIntegerField(default=2)


class Vehicle(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="owner")
    driver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="driver")
    vehicle_no = models.CharField(max_length=40)


class Driver_recieve_portal(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    amount = models.FloatField()
    reason = models.TextField()


class Driver_pay_portal(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    amount = models.FloatField()
    reason = models.TextField()


class Comment(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    text = models.CharField(max_length=256)
