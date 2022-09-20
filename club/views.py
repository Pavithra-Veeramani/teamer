from django.shortcuts import render, redirect, reverse
from .models import Event
from django.views.generic import View
from .models import Member

from django.contrib.auth import get_user_model


""""Views to get members"""

def get_member(request):
    members = Member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'member/member.html', context)

"""Views to create new event"""
def add_event(request):
    return render(request, 'event/add.html')

"""Submit create new event
"""
def submit_add_event(request):
    name = request.POST.get('name')
    place = request.POST.get('place')
    date = request.POST.get('date')
    time = request.POST.get('time')
    member = Member.objects.filter(user=request.user).first()
    created_by = member

    print('submit event', place)
    Event.objects.create(
        name=name, place=place, date=date, time=time, created_by=created_by
        )
    context = {
        'message': 'You have successfully created an event.'
    }
    return render(request, 'event/event_action_success.html', context)

""""""
def get_home(request):
    return render(request, 'index.html')


def get_events(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        date = request.POST.get('date')
        time = request.POST.get('time')
        Event.objects.create(name=name, place=place, date=date, time=time)
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'event/event.html', context)


def delete_event(request, id):
    Event.objects.filter(id=id).delete()
    context = {
        'message': 'Event deleted successfully.'
    }
    return render(request, 'event/event_action_success.html', context)


def get_event_details(request, id):
    event = Event.objects.get(pk=id)
    members = event.members.all()
    logged_member = member = Member.objects.filter(user=request.user).first()
    print('Event from DB:', event)
    context = {
        'event': event,
        'members': members,
        'current_member': logged_member
    }
    return render(request, 'event/details.html', context)


def add_member_to_event(request, id):
    print('adding')
    member = Member.objects.filter(user=request.user).first()
    event = Event.objects.get(pk=id)
    event.members.add(member)
    event = Event.objects.get(pk=id)
    members = event.members.all()

    context = {
        'message': 'You have been successfully added to the event.'
    }
    return render(request, 'event/event_action_success.html', context)


def delete_member_from_event(request, id):
    ('deleting')
    member = Member.objects.filter(user=request.user).first()
    event = Event.objects.get(pk=id)
    event.members.remove(member)
    members = event.members.all()

    context = {
        'message': 'You have successfully deleted the event.'
    }
    return render(request, 'event/event_action_success.html', context)


class CreateMember(View):
    template_name = "create_member.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "member/create_member.html",
        )

    def post(self, request):
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        email = request.POST.get("email")
        tele = request.POST.get("phone_number")

        member = Member.objects.create(
            first_name=f_name,
            last_name=l_name,
            phone_number=tele,
            email=email,
            user=request.user,
        )

        member.save()

        return redirect(reverse('home'))
