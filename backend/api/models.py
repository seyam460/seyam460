from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        RIDER = 'rider', 'Rider'
        DRIVER = 'driver', 'Driver'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.RIDER)
    phone_number = models.CharField(max_length=20, blank=True)


class Ride(models.Model):
    class Status(models.TextChoices):
        REQUESTED = 'requested', 'Requested'
        ACCEPTED = 'accepted', 'Accepted'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'
        CANCELED = 'canceled', 'Canceled'

    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides')
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='drives')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.REQUESTED)
    pickup_address = models.CharField(max_length=255)
    dropoff_address = models.CharField(max_length=255)
    pickup_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    pickup_lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    dropoff_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    dropoff_lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    distance_km = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    price_estimate = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    actual_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)


class TrackPoint(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='track_points')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    recorded_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PAID = 'paid', 'Paid'
        FAILED = 'failed', 'Failed'

    ride = models.OneToOneField(Ride, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    provider = models.CharField(max_length=50, default='mock')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    transaction_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
