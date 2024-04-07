from django.db import models
from django.contrib.auth.models import AbstractUser


# ==========================================  
#           UserProfile Module
# ========================================== 

class CustomUser(AbstractUser):
   aadhar_no = models.CharField(max_length=12, unique=True)
   profile_img = models.ImageField(upload_to='profile_images/', blank=True, null=True)

   full_name = models.CharField(max_length=100, blank=True, null=True, default="")
   dob = models.DateField(blank=True, null=True, default=None)
   age = models.IntegerField(blank=True, null=True, default=0)

   GENDER_CHOICES = [
      ('M', 'Male'),
      ('F', 'Female'),
      ('O', 'Other'),
   ]
   gender = models.CharField(max_length=1, choices = GENDER_CHOICES, blank=True, null=True, default="")
   
   address = models.TextField(max_length=100, blank=True, null=True,)

   mobile_no = models.CharField(max_length=100, blank=True, null=True, default="")
   aadhar_img = models.ImageField(upload_to='aadhar_images/', blank=True, null=True)
   father = models.CharField(max_length=100, blank=True, null=True, default="")
   mother = models.CharField(max_length=255, blank=True, null=True, default="")

   MARITAL_STATUS_CHOICES = [
      ('S', 'Single'),
      ('M', 'Married'),
   ]
   marital_status = models.CharField(max_length=1, choices = MARITAL_STATUS_CHOICES, blank=True, null=True, default="")

   children_no = models.IntegerField(blank=True, null=True, default=0)

   EMPLOYMENT_STATUS_CHOICES = [
      ('Emp', 'Employed'),
      ('Unemp', 'Unemployed'),
      ('Self-emp', 'Self-employed'),
      ('Stud', 'Student'),
      ('Ret', 'Retired'),
   ]
   employment_status = models.CharField(max_length=10, choices=EMPLOYMENT_STATUS_CHOICES, blank=True, null=True, default="")
 
   OCCUPATION_CHOICES = [
        ('Government_Employee', 'Government Employee'),
        ('Accountant', 'Accountant'),
        ('Actor/Actress', 'Actor/Actress'),
        ('Architect', 'Architect'),
        ('Artist', 'Artist'),
        ('Baker', 'Baker'),
        ('Banker', 'Banker'),
        ('Barista', 'Barista'),
        ('Bartender', 'Bartender'),
        ('Biologist', 'Biologist'),
        ('Carpenter', 'Carpenter'),
        ('Chef', 'Chef'),
        ('Cleaner', 'Cleaner'),
        ('Computer_Programmer', 'Computer Programmer'),
        ('Dentist', 'Dentist'),
        ('Doctor', 'Doctor'),
        ('Electrician', 'Electrician'),
        ('Engineer', 'Engineer'),
        ('Farmer', 'Farmer'),
        ('Firefighter', 'Firefighter'),
        ('Fisherman', 'Fisherman'),
        ('Flight_Attendant', 'Flight Attendant'),
        ('Graphic_Designer', 'Graphic Designer'),
        ('Hairdresser', 'Hairdresser'),
        ('Journalist', 'Journalist'),
        ('Lawyer', 'Lawyer'),
        ('Librarian', 'Librarian'),
        ('Mechanic', 'Mechanic'),
        ('Musician', 'Musician'),
        ('Nurse', 'Nurse'),
        ('Pharmacist', 'Pharmacist'),
        ('Photographer', 'Photographer'),
        ('Pilot', 'Pilot'),
        ('Plumber', 'Plumber'),
        ('Police_Officer', 'Police Officer'),
        ('Professor', 'Professor'),
        ('Psychologist', 'Psychologist'),
        ('Real_Estate_Agent', 'Real Estate Agent'),
        ('Receptionist', 'Receptionist'),
        ('Scientist', 'Scientist'),
        ('Software_Developer', 'Software Developer'),
        ('Teacher', 'Teacher'),
        ('Truck_Driver', 'Truck Driver'),
        ('Veterinarian', 'Veterinarian'),
        ('Waiter/Waitress', 'Waiter/Waitress'),
        ('Writer', 'Writer'),
    ]
   occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES, blank=True, null=True, default="")
   
   monthly_income = models.FloatField(blank=True, null=True, default=0)

   
   EDUCATION_CHOICES = [
        ('Primary', 'Primary School'),
        ('Secondary', 'Secondary School'),
        ('High', 'High School'),
        ('Dip', 'Diploma'),
        ("Bachelors", "Bachelor's Degree"),
        ("Masters", "Master's Degree"),
        ('Doctorate', 'Doctorate'),
    ]
   highest_education = models.CharField(max_length=15, choices=EDUCATION_CHOICES, blank=True, null=True, default="")
   
   highest_education_mark = models.FloatField(blank=True, null=True, default=0)

   
   CASTE_CHOICES = [
        ('SC', 'Scheduled Caste (SC)'),
        ('ST', 'Scheduled Tribe (ST)'),
        ('OBC', 'Other Backward Class (OBC)'),
        ('General', 'General'),
        ('Prefer_not_to_say', 'Prefer not to say'),
    ]
   caste = models.CharField(max_length=20, choices=CASTE_CHOICES, blank=True, null=True, default="")
    
   RELIGION_CHOICES = [
        ('Hin', 'Hinduism'),
        ('Isl', 'Islam'),
        ('Chr', 'Christianity'),
        ('Sik', 'Sikhism'),
        ('Bud', 'Buddhism'),
        ('Jai', 'Jainism'),
    ]
   religion = models.CharField(max_length=15, choices=RELIGION_CHOICES, blank=True, null=True, default="")
   
   DISABILITY_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
   has_disabilities = models.CharField(max_length=3, choices=DISABILITY_CHOICES, blank=True, null=True, default="")
   disabilities_specify = models.CharField(max_length=255, blank=True, null=True, default="_")
   
   bank_name = models.CharField(max_length=255, blank=True, null=True, default="")
   account_number = models.CharField(max_length=50, blank=True, null=True, default="")
   ifsc_code = models.CharField(max_length=20, blank=True, null=True, default="")
   
   identity_img = models.FileField(upload_to='identity_images/', blank=True, null=True )

   verified_flag = models.BooleanField(default=False)
   profile_updated_flag = models.BooleanField(default=False)
   reg_date = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
        return self.username
   
   

# ==========================================  
#              Ask Quary
# ==========================================   

# class AskQuery(models.Model):    
#     q_email = models.EmailField(blank=True, null=True, default=None)
#     q_name = models.CharField(max_length=255, blank=True, null=True, default=None)
#     q_mobile = models.CharField(max_length=255, blank=True, null=True, default=None)
#     q_query = models.TextField(max_length=255, blank=True, null=True, default=None)
#     q_submit_date = models.DateField(blank=True, null=True, default=None)
#     q_flag = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.name
