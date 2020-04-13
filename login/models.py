from django.db import models
import django.contrib.auth
from django.utils import timezone

# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length=20, null=False, blank=False)
    LastName = models.CharField(max_length=20, null=False, blank=False)
    Email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    Mobile = models.IntegerField(null=False, blank=False)
    Username = models.CharField(max_length=100, null=False, blank=False)
    CreatedAt = models.DateTimeField(default=timezone.now)
    UpdatedAt = models.DateTimeField(default=timezone.now)