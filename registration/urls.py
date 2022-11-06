from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name='index'),
    path('login',views.login,name='login'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('patient',views.patient,name='patient'),
    path('medstaff',views.medstaff,name='medstaff'),
    path('adminpage/register/patient',views.registerpatient,name='registerpatient'),
    path('adminpage/register/doctor',views.registerdoctor,name='registerdoctor'),
    path('adminpage/patientlist',views.patientlist,name='patientlist'),
    path('adminpage/doctorlist',views.doctorlist,name='doctorlist'),
    path('adminpage/deletepatient/<int:id>', views.deletepatient, name='deletepatient'),
    path('adminpage/updatepatient/<int:id>', views.updatepatient, name='updatepatient'),
    path('adminpage/updatepatient/updaterecord/<int:id>', views.updatepatientrecord, name='updatepatientrecord'),
    path('adminpage/deletedoctor/<int:id>', views.deletedoctor, name='deletedoctor'),
    path('adminpage/updatedoctor/<int:id>', views.updatedoctor, name='updatedoctor'),
    path('adminpage/updatedoctor/updaterecord/<int:id>', views.updatedoctorrecord, name='updatedoctorrecord')
]