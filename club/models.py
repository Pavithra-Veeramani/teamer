from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    '''
        Model for Member entity.
        This has a one to one relation with django account User object
    '''
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=12)
    position = models.CharField(max_length=15, null=True, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
        )

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    '''
        Model for Event entity.
        This has a many to many relation with the member table
    '''
    name = models.CharField(max_length=50, null=False, blank=False)
    place = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="owner"
        )
    members = models.ManyToManyField(
        Member, related_name='players_in_event', blank=True
        )

    def __str__(self):
        return self.name + ' ' + self.place + ' '
