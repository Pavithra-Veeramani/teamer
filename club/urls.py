"""teamer_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
from club.views import get_member, get_home, submit_add_member, get_events, add_event, get_event_details, add_member_to_event


urlpatterns = [
    path('', get_home, name='home'),
    path('member/', get_member, name='member-page'),
    path('submitaddmember', submit_add_member, name='submitaddmember-page'),
    path('accounts/', include('allauth.urls')),
    path('event/', get_events, name='events-page'),
    path('event/<int:id>', get_event_details, name='get_event_details'),
    path('event/<int:id>/member/', add_member_to_event, name='add_member_to_event'),
    path('addevent/', add_event, name='addevent-page'),
]