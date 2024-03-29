"""pericles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.BASE, name='base'),

                  # Login Path
                  path('', views.LOGIN, name='login'),
                  path('doLogin', views.doLogin, name='doLogin'),
                  path('doLogout', views.doLogout, name='logout'),

                  # profile update
                  path('profile', views.PROFILE, name='profile'),
                  path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

                  # This is HOD panel urls
                  path('hod/home', Hod_Views.HOME, name='hod_home'),
                  path('hod/student/add', Hod_Views.ADD_STUDENT, name='add_student'),
                  path('hod/student/view', Hod_Views.VIEW_STUDENT, name='view_student'),
                  path('staff/home', Staff_Views.HOME, name='staff_home'),
                  path('student/home', Student_Views.HOME, name='student_home'),
                  path('staff/add', Staff_Views.ADD_TEACHER, name='add_teacher'),
                  path('staff/view', Staff_Views.VIEW_TEACHER, name='view_teacher'),
                  path('staff/edit', Staff_Views.EDIT_TEACHER, name='edit_teacher'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
