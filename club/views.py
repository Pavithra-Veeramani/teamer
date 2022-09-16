from django.shortcuts import render, redirect, reverse
from .models import Event
from django.views.generic import View

from django.contrib.auth import get_user_model

def get_member(request):
    #members = Member.objects.all()
    User = get_user_model()
    users = User.objects.all()
    context = {
        'members': users
    }
    return render(request, 'member/member.html', context)

def add_event(request):
    return render(request, 'event/add.html')

def submit_add_event(request):
    name = request.POST.get('name')
    place = request.POST.get('place')
    date = request.POST.get('date')
    time = request.POST.get('time')
    created_by = request.user

    print('submit event', place)
    Event.objects.create(name=name, place=place, date=date, time=time, created_by=created_by)
    context = {
        'message': 'You have successfully created an event'
    }
    #return redirect(reverse('events-page'))
    return render(request, 'success.html', context)


def get_home(request):
    return render(request, 'index.html')

def get_events(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        date = request.POST.get('date')
        time = request.POST.get('time')
        Event.objects.create(name=name, place=place,date=date, time=time)
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'event/event.html', context)

def delete_event(request):
    print(request.POST.get('id'))
    context = {
        'message': 'Event deleted successfully'
    }
    return render(request, 'success.html', context)

def get_event_details(request, id):
    event = Event.objects.get(pk=id)
    members = event.members.all()
    print('Event from DB:', event)
    context = {
        'event': event,
        'members': members
    }
    return render(request, 'event/details.html', context)

def add_member_to_event(request, id):
    print('adding')
    event = Event.objects.get(pk=id)
    event.members.add(request.user)
    #event.save()
    event = Event.objects.get(pk=id)
    members = event.members.all()

    context = {
        'event': event,
        'members': members
    }
    return render(request, 'event/details.html', context)

def delete_member_from_event(request, id):
    ('deleting')
    event = Event.objects.get(pk=id)
    event.members.remove(request.user)
    #event.save()
    members = event.members.all()

    context = {
        'event': event,
        'members': members
    }
    return render(request, 'event/details.html', context)

class MemberEventView(View):
    http_method_names = ['get', 'post', 'delete']

    def post(self, *args, **kwargs):
        print(self.request.method)

    def delete(self, *args, **kwargs):
        print('dfgdf')
        print(self.request.method)
    
    def get(self, *args, **kwargs):
        print('dfgdf')
        print(self.request.method)