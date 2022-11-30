from django.urls import path
from . import views
from django.views.generic import TemplateView
from rest_framework import routers
from .views import DoctorViewSet

#router=routers.DefaultRouter
#router.register(r'api/doctors',DoctorViewSet,'doctors')

urlpatterns=[
    #path('appointment',views.appointment,name='appointment'),
    path('', views.index,name='index'),
    path('login',views.login,name='login'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('patient/<str:iin_num>',views.patient,name='patient'),
    path('doctor/<str:iin_num>',views.medstaff,name='medstaff'),
    path('adminpage/register/patient',views.registerpatient,name='registerpatient'),
    path('adminpage/register/doctor',views.registerdoctor,name='registerdoctor'),
    path('adminpage/patientlist',views.patientlist,name='patientlist'),
    path('adminpage/doctorlist',views.doctorlist,name='doctorlist'),
    path('adminpage/deletepatient/<int:id>', views.deletepatient, name='deletepatient'),
    path('adminpage/updatepatient/<int:id>', views.updatepatient, name='updatepatient'),
    path('adminpage/updatepatient/updaterecord/<int:id>', views.updatepatientrecord, name='updatepatientrecord'),
    path('adminpage/deletedoctor/<int:id>', views.deletedoctor, name='deletedoctor'),
    path('adminpage/updatedoctor/<int:id>', views.updatedoctor, name='updatedoctor'),
    path('adminpage/updatedoctor/updaterecord/<int:id>', views.updatedoctorrecord, name='updatedoctorrecord'),
    path('patient/<str:iin_num>/appointment',views.appointment,name='appointment'),
    path('jai',views.jai,name='jai')
]