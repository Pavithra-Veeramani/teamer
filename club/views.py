from django.shortcuts import render
from .models import Event

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

def submit_add_member(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    Member.objects.create(first_name=fname, last_name=lname,email=email)
    return render(request, 'member/addsuccess.html')


def get_home(request):
    return render(request, 'index.html')

def get_events(request):
    events = Event.objects.all()

    # for event in events:
    #     print('Members ', event.members.all())

    context = {
        'events': events
    }
    return render(request, 'event/event.html', context)

def get_event_details(request, id):
    event = Event.objects.get(pk=id)
    members = list(event.members.all())
    print('Event from DB:', event)
    context = {
        'event': event,
        'members': members
    }
    return render(request, 'event/details.html', context)

def add_member_to_event(request, id):
    print('Adding members ', request.user)
    event = Event.objects.get(pk=id)
    print('Adding members ', event)
    print('Adding members ', event.players_in_event_set)
    event.players_in_event_set.add(request.user)
    #event.save()
    event = Event.objects.get(pk=id)
    print('Adding members ', event.players_in_event_set)

    context = {
        'event': event
    }
    return render(request, 'event/details.html', context)