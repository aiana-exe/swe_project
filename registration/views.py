from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest,Http404,HttpResponseRedirect
from .models import Admin
from .models import Medical_staff
from .models import Patient
from .models import Specialization_details
from .models import Department
from django.contrib import messages
from django.urls import reverse
from django.template import loader
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DoctorSerializer,SpecSerializer
from rest_framework import viewsets
import json
from django.forms.models import model_to_dict
from json import dumps
from django.core import serializers
#from r.views import APIView
#import model
#create an object for the class

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class=DoctorSerializer
    queryset=Medical_staff.objects.all()


def index(request):
    return render(request,'indexx.html')


@api_view(['GET','POST'])
def appointment(request,iin_num):
    #doctors=dumps(list(Medical_staff.objects.values('full_name')))
    #for item in doctoraw:
    #    item['product'] = model_to_dict(item['product'])
    #serializer=DoctorSerializer(doctoraw,many=True)
    #context={
    #    '':doctors
    #}
    #return Response(serializer.data)
    #doctors = json.dumps(list(doctoraw))
    #context = {'doctors': doctors}
    #doctors = serializers.serialize('json', doctoraw, fields=())
    #doctors=dumps(doctoraw)
    #return render(request,'index.html',{'doctors':doctors})
    doctors=Medical_staff.objects.all()
    specialization=Specialization_details.objects.all()
    specSer=SpecSerializer(specialization,many=True)
    serializer=DoctorSerializer(doctors,many=True)
    return Response({'doctors':serializer.data,'specialization':specSer.data})
    #return Response({serializer.data})
@api_view(['GET'])
def jai(request):
    doctors=Medical_staff.objects.all()
    serializer=DoctorSerializer(doctors,many=True)
    return Response(serializer.data)


def login(request):
    if request.method=='POST':
        try:
            user1=Admin.objects.get(username=request.POST.get('username'),password=request.POST.get('password'))
        except:
            try:
                user1=Patient.objects.get(iin_num=request.POST.get('username'),password=request.POST.get('password'))
            except:
                try:
                    user1=Medical_staff.objects.get(iin_num=request.POST.get('username'),password=request.POST.get('password'))
                except:
                    messages.info(request,'Credentials Invalid')
                else:
                    str='doctor/'+request.POST.get('username')
                    return redirect('doctor',iin_num=request.POST.get('username'))
            else:
                str='patient/'+request.POST.get('username')
                #return redirect('patient/<int:iin_num>', {'iin_num':request.POST.get('username')})
                iin_num=request.POST.get('username')
                print(iin_num)
                return redirect(str,iin_num=iin_num)
        else:
            return redirect('adminpage')
        #username=request.POST['username']
        #password=request.POST['password']
    #user1=Admin.objects.get(username=request.POST.get('username'),password=request.POST.get('password'))
    return render(request,'login.html')

#@login_required
def adminpage(request):
    all_patients=Patient.objects.all()
    return render(request,'adminpage.html',{'all_patients':all_patients})

#@login_required
def patient(request,iin_num):
    print(iin_num)
    patient=Patient.objects.get(iin_num=iin_num)
    context={
    'patient':patient
    }
    return render(request,'patient.html',context)


#@login_required
def medstaff(request,iin_num):
    doctor=Medical_staff.objects.get(iin_num=iin_num)
    context={
        'doctor':doctor
    }
    return render(request,'medstaff.html',context)

def registerpatient(request):
    marital_status=['single','widowed','married','separated','divorced']
    blood_group=['A','B','AB','O']
    context={
        'marital_status':marital_status,
        'blood_group':blood_group
    }
    if request.method=='POST':
        birthdate=request.POST.get('birthdate')
        iin=request.POST.get('iin')
        fullname=request.POST.get('fullname')
        bloodgroup=request.POST.get('bloodgroup')
        emergcontact=request.POST.get('emergcontact')
        contactnum=request.POST.get('contactnum')
        email=request.POST.get('email')
        address=request.POST.get('address')
        marital_status=request.POST.get('marital_status')
        regdate=request.POST.get('regdate')
        password=request.POST.get('password')
        patient=Patient(marital_status=marital_status,date_of_birth=birthdate,iin_num=iin,full_name=fullname,blood_group=bloodgroup,emergency_cont_num=emergcontact,contact_num=contactnum,email=email,address=address,registration_date=regdate,password=password)
        if not Patient.objects.filter(iin_num=iin).exists():
            patient.save()
            return redirect('patientlist')
    return render(request,'registerpatient.html',context)

def registerdoctor(request):
    educ=['Bachelor','Master','Doctor']
    rating=[1,2,3,4,5,6,7,8,9,10]
    category=['Highest','First','Second']
    specialization=Specialization_details.objects.all()
    departments=Department.objects.all()
    context={
        'educ':educ,
        'rating':rating,
        'category':category,
        'specialization':specialization,
        'departments':departments
    }
    if request.method=='POST':
        if len(request.FILES)!=0:
            photo=request.FILES['photo']
        birthdate=request.POST.get('birthdate')
        iin=request.POST.get('iin')
        fullname=request.POST.get('fullname')
        #id_num=request.POST.get('id')
        department_id=request.POST.get('department_id')
        contactnum=request.POST.get('contactnum')
        specialization_details_id=request.POST.get('specialization_details_id')
        experience=request.POST.get('experience')
        category=request.POST.get('category')
        password=request.POST.get('password')
        price_of_appointment=request.POST.get('price_of_appointment')
        schedule_details=request.POST.get('schedule_details')
        education_degree=request.POST.get('education_degree')
        rating=request.POST.get('rating')
        address=request.POST.get('address')
        if len(request.FILES)!=0:
            doctor=Medical_staff(rating=rating,date_of_birth=birthdate,iin_num=iin,full_name=fullname,education_degree=education_degree,schedule_details=schedule_details,contact_num=contactnum,price_of_appointment=price_of_appointment,category=category,photo=photo,password=password,experience=experience,specialization_details_id_id=specialization_details_id,department_id_id=department_id,address=address)
        else:
            doctor=Medical_staff(rating=rating,date_of_birth=birthdate,iin_num=iin,full_name=fullname,education_degree=education_degree,schedule_details=schedule_details,contact_num=contactnum,price_of_appointment=price_of_appointment,category=category,password=password,experience=experience,specialization_details_id_id=specialization_details_id,department_id_id=department_id,address=address)
        if not Medical_staff.objects.filter(iin_num=iin).exists():
            doctor.save()
            return redirect('doctorlist')
    return render(request,'registerdoctor.html',context)

def patientlist(request):
    all_patients=Patient.objects.all()
    return render(request,'patientlist.html',{'all_patients':all_patients})
def doctorlist(request):
    all_doctors=Medical_staff.objects.all()
    return render(request,'doctorlist.html',{'all_doctors':all_doctors})

def deletepatient(request, id):
  patient = Patient.objects.get(id=id)
  patient.delete()
  #return render(request,'patientlist.html')
  return HttpResponseRedirect(reverse('patientlist'))

def deletedoctor(request, id):
  doctor = Medical_staff.objects.get(id=id)
  doctor.delete()
  #return render(request,'patientlist.html')
  return HttpResponseRedirect(reverse('doctorlist'))


def updatepatient(request, id):
  patient = Patient.objects.get(id=id)
  template = loader.get_template('updatepatient.html')
  context = {
    'patient': patient,
  }
  return HttpResponse(template.render(context, request))

def updatedoctor(request, id):
  doctor = Medical_staff.objects.get(id=id)
  template = loader.get_template('updatedoctor.html')
  context = {
    'doctor': doctor,
  }
  return HttpResponse(template.render(context, request))

def updatepatientrecord(request, id):
  full_name = request.POST['full_name']
  marital_status = request.POST['marital_status']
  birthdate=request.POST['birthdate']
  iin=request.POST['iin']
  bloodgroup=request.POST['bloodgroup']
  emergcont=request.POST['emergcont']
  cont=request.POST['cont']
  email=request.POST['email']
  address=request.POST['address']
  regdate=request.POST['regdate']
  password=request.POST['password']
  
  member = Patient.objects.get(id=id)
  member.full_name = full_name
  member.marital_status = marital_status
  member.date_of_birth = birthdate
  member.iin_num = iin
  member.blood_group = bloodgroup
  member.emergency_cont_num = emergcont
  member.contact_num = cont
  member.email = email
  member.address = address
  member.registration_date = regdate
  member.password = password
  member.save()
  return HttpResponseRedirect(reverse('patientlist'))

def updatedoctorrecord(request, id):
  full_name = request.POST['full_name']
  rating = request.POST['rating']
  birthdate=request.POST['birthdate']
  iin=request.POST['iin']
  education_degree=request.POST['education_degree']
  schedule_details=request.POST['schedule_details']
  cont=request.POST['cont']
  price_of_appointment=request.POST['price_of_appointment']
  address=request.POST['address']
  category=request.POST['category']
  password=request.POST['password']
  photo=request.POST['photo']
  experience=request.POST['experience']
  specialization_details_id=request.POST['specialization_details_id']
  department_id=request.POST['department_id']
  id_num=request.POST['id_num']
  
  member = Medical_staff.objects.get(id=id)
  member.full_name = full_name
  member.rating = rating
  member.date_of_birth = birthdate
  member.iin_num = iin
  member.education_degree = education_degree
  member.schedule_details = schedule_details
  member.contact_num = cont
  member.price_of_appointment = price_of_appointment
  member.address = address
  member.category = category
  member.password = password
  member.photo = photo
  member.experience = experience
  member.specialization_details_id_id =specialization_details_id
  member.department_id_id = department_id
  member.id_num = id_num
  member.save()
  return HttpResponseRedirect(reverse('doctorlist'))

