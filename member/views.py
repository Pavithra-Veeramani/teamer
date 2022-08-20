from django.shortcuts import render
from .models import Member

def get_member(request):
    members = Member.objects.all();
    context = {
        'members': members
    }
    return render(request, 'member/member.html', context)

def add_member(request):
    return render(request, 'member/add.html')

def submit_add_member(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    Member.objects.create(first_name=fname, last_name=lname,email=email)
    return render(request, 'member/addsuccess.html')


def get_home(request):
    return render(request, 'index.html')