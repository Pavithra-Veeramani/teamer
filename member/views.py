from django.shortcuts import render
from .models import Member

def get_member(request):
    members = Member.objects.all();
    context = {
        'members': members
    }
    return render(request, 'member/member.html', context)

def get_home(request):
    return render(request, 'index.html')