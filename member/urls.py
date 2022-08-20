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

from django.urls import path
from member.views import get_member, get_home, add_member, submit_add_member


urlpatterns = [
    path('', get_home, name='home'),
    path('member/', get_member, name='member-page'),
    path('addmember/', add_member, name='addmember-page'),
    path('submitaddmember', submit_add_member, name='submitaddmember-page')
]
