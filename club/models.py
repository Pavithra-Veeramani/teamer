from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Member(models.Model):
#     first_name = models.CharField(max_length=50, null=False, blank=False)
#     last_name = models.CharField(max_length=50, null=False, blank=False)
#     email = models.CharField(max_length=50, null=False, blank=False)

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    place = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    members = models.ManyToManyField(User, related_name='players_in_event', blank=True)

    def __str__(self):
        return self.name + ' ' + self.place + ' '
