"""testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from studentapp.views import index,studentform,delstudent,updatestd,schoolform,viewschoollist,scfulldetails,delschool,updatesc,stdschdetail,viewstdlist,test,standardlist,attendancelist,viewattendancelist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),

    #This below part is for student

    path('studentform',studentform,name="studentform"),
    path('stdschdetail/<int:id>',stdschdetail,name="stdschdetail"),
    path('updatestd/<int:id>',updatestd,name="updatestd"),
    path('delstudent/<int:id>',delstudent,name="delstudent"),



    path('standardlist/<int:id>', standardlist, name="standardlist"),
    path('viewstdlist/<int:scid>/<int:id>',viewstdlist,name="viewstdlist"),



    #this below part is for school

    path('schoolform',schoolform,name="schoolform"),
    path('viewschoollist', viewschoollist, name="viewschoollist"),
    path('scfulldetails/<int:id>', scfulldetails, name="scfulldetails"),
    path('updatesc/<int:id>', updatesc, name="updatesc"),
    path('delschool/<int:id>', delschool, name="delschool"),


    #below pat for attendance
    path('attendancelist/<int:scid>/<int:id>',attendancelist,name="attendancelist"),
    path('viewattendancelist/<int:scid>/<int:id>',viewattendancelist,name="viewattendancelist"),


    #this is dor testing purpose
    path('testing',test, name="testing")

]