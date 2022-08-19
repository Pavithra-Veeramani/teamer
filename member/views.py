from django.shortcuts import render


def get_member(request):
    return render(request, 'member/member.html')

def get_home(request):
    return render(request, 'index.html')