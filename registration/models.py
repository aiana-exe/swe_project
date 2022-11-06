from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Patient(models.Model):
    '''MARITAL_STATUS_CHOICES=[
        ('SINGLE','SINGLE'),
        ('MARRIED','MARRIED'),
        ('WIDOWED','WIDOWED'),
        ('SEPARATED','SEPARATED'),
        ('DIVORCED','DIVORCED')
    ]'''

    date_of_birth=models.DateField()
    iin_num=models.CharField(max_length=12)
    id_num=models.AutoField().primary_key
    full_name=models.CharField(max_length=50)
    blood_group=models.CharField(max_length=2)
    emergency_cont_num=models.CharField(max_length=11)
    contact_num=models.CharField(max_length=11)
    email=models.EmailField()
    #department_id=models.ForeignKey('Department',on_delete=models.CASCADE,)
    #specialization_details_id=models.ForeignKey('Specialization_details',on_delete=models.CASCADE,)
    #experience=models.IntegerField()
    #photo=models.ImageField()
    #category=models.CharField(max_length=15)
    #price_of_appointment=models.IntegerField()
    #schedule_details=models.CharField(max_length=100)
    #education_degree=models.CharField(max_length=10)
    #rating=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)])
    address=models.CharField(max_length=20)
    #marital_status=models.CharField(max_length=10)
    registration_date=models.DateField()
    password=models.CharField(max_length=30)
    marital_status=models.CharField(max_length=15)

class Medical_staff(models.Model):
    date_of_birth=models.DateField()
    iin_num=models.CharField(max_length=12)
    id_num=models.AutoField().primary_key
    full_name=models.CharField(max_length=50)
    contact_num=models.CharField(max_length=11)
    department_id=models.ForeignKey('Department',on_delete=models.CASCADE,)
    specialization_details_id=models.ForeignKey('Specialization_details',on_delete=models.CASCADE,)
    experience=models.IntegerField()
    photo=models.ImageField()
    category=models.CharField(max_length=15)
    price_of_appointment=models.IntegerField()
    schedule_details=models.CharField(max_length=100)
    education_degree=models.CharField(max_length=10)
    rating=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)])
    address=models.CharField(max_length=20)
    password=models.CharField(max_length=30)

class Admin(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=40)

class Department(models.Model):
    department_id=models.AutoField().primary_key

class Specialization_details(models.Model):
    specialization_details_id=models.AutoField().primary_key