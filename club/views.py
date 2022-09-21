from django.shortcuts import render, redirect, reverse
from .models import Event
from django.views.generic import View
from .models import Member
from .forms import EditMemberForm

from django.contrib.auth import get_user_model


def get_member(request):
    '''
        View method to fetch all the members from the DB
    '''
    members = Member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'member/member.html', context)


def add_event(request):
    '''
        View method to launch Create event page
    '''
    return render(request, 'event/add.html')


def submit_add_event(request):
    '''
        View method to save event in the DB
    '''
    name = request.POST.get('name')
    place = request.POST.get('place')
    date = request.POST.get('date')
    time = request.POST.get('time')
    member = Member.objects.filter(user=request.user).first()
    created_by = member

    Event.objects.create(
        name=name, place=place, date=date, time=time, created_by=created_by
        )
    context = {
        'message': 'You have successfully created an event.'
    }
    return render(request, 'event/event_action_success.html', context)


def get_home(request):
    '''
        View method to launch Home page
    '''
    return render(request, 'index.html')


def get_events(request):
    '''
        View method to load all the events from the DB
    '''
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
    '''
        View method to delete an event in the DB
    '''
    Event.objects.filter(id=id).delete()
    context = {
        'message': 'Event deleted successfully.'
    }
    return render(request, 'event/event_action_success.html', context)


def get_event_details(request, id):
    '''
        View method to load the details of an event from the DB
    '''
    event = Event.objects.get(pk=id)
    members = event.members.all()
    logged_member = member = Member.objects.filter(user=request.user).first()
    context = {
        'event': event,
        'members': members,
        'current_member': logged_member
    }
    return render(request, 'event/details.html', context)


def add_member_to_event(request, id):
    '''
        View method to add a member to an event.
        This creates a record in the event_members table
    '''
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
    '''
        View method to delete a member from an event.
        This deletes a record in the event_members table
    '''
    member = Member.objects.filter(user=request.user).first()
    event = Event.objects.get(pk=id)
    event.members.remove(member)
    members = event.members.all()

    context = {
        'message': 'You have successfully deleted the event.'
    }
    return render(request, 'event/event_action_success.html', context)


class CreateMember(View):
    '''
        View to create a new member.
        This creates a record in the members table
    '''
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
        position = request.POST.get("position")

        member = Member.objects.create(
            first_name=f_name,
            last_name=l_name,
            phone_number=tele,
            email=email,
            position=position,
            user=request.user,
        )

        member.save()

        return redirect(reverse('home'))

class EditMember(View):
    model = Member()
    template_name = "member/edit_member.html"
    context_object_name = 'edit_member'

    def get(self, request, user, *args, **kwargs):
        member = Member.objects.filter(user=user).first()
        if member is None:
            return redirect(reverse('create_member'))

        return render(
            request,
            "member/edit_member.html",
            {
                "member": member,
                "updated": False,
                "Edit_MemberForm": EditMemberForm(instance=member)
            },
        )

    def post(self, request, user, *args, **kwargs):
        member = Member.objects.get(user=user)

        edit_member_form = EditMemberForm(request.POST, instance=member)

        if edit_member_form.is_valid():
            edit_member_form.save()
        else:
            edit_member_form = EditMemberForm(instance=member)

        return render(
            request,
            "member/edit_member.html",
            {
                "member": member,
                'updated': True,
                "Edit_MemberForm": edit_member_form
            },
        )
