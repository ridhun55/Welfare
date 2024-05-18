from django.db import models
from django.contrib.auth.models import AbstractUser
from UserApp.models import CustomUser


# ==========================================  
#           Welfare Post Module
# ========================================== 

class WelfarePost(models.Model):
   post_title = models.CharField(max_length=120, blank=True, null=True)
   post_description = models.TextField(blank=True, null=True)
   post_img = models.ImageField(upload_to='welfare_images/', blank=True, null=True)
   post_age = models.IntegerField(blank=True, null=True, default=0)


   POST_CATEGORY_CHOICES = [
      ('Education', 'Education'),
      ('Healthcare', 'Healthcare'),
      ('Employment', 'Employment'),
      ('Housing', 'Housing'),
      ('Rural_Development', 'Rural Development'),
      ('Minority_Welfare', 'Minority Welfare'),
   ]
   post_category = models.CharField(max_length=60, choices = POST_CATEGORY_CHOICES, blank=True, null=True, default="")
   
   GENDER_CHOICES = [
      ('M', 'Male'),
      ('F', 'Female'),
      ('O', 'Other'),
      ('All', 'All'),
   ]
   post_gender = models.CharField(max_length=3, choices = GENDER_CHOICES, blank=True, null=True, default="")

   MARITAL_STATUS_CHOICES = [
      ('S', 'Single'),
      ('M', 'Married'),
      ('Both', 'Both'),
   ]
   post_marital_status = models.CharField(max_length=5, choices = MARITAL_STATUS_CHOICES, blank=True, null=True, default="")

   post_children = models.IntegerField(blank=True, null=True, default=0)

   EMPLOYMENT_STATUS_CHOICES = [
      ('Emp', 'Employed'),
      ('Unemp', 'Unemployed'),
      ('Self-emp', 'Self-employed'),
      ('Stud', 'Student'),
      ('Ret', 'Retired'),
      ('All', 'All'),
   ]
   post_employment_status = models.CharField(max_length=10, choices=EMPLOYMENT_STATUS_CHOICES, blank=True, null=True, default="")
 
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
        ('All', 'All'),
    ]
   post_occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES, blank=True, null=True, default="")
   
   post_monthly_income = models.FloatField(blank=True, null=True, default=0)
   
   EDUCATION_CHOICES = [
        ('Primary', 'Primary School'),
        ('Secondary', 'Secondary School'),
        ('High', 'High School'),
        ('Dip', 'Diploma'),
        ("Bachelors", "Bachelor's Degree"),
        ("Masters", "Master's Degree"),
        ('Doctorate', 'Doctorate'),
        ('All', 'All'),
    ]
   post_highest_education = models.CharField(max_length=15, choices=EDUCATION_CHOICES, blank=True, null=True, default="")
   
   post_highest_education_mark =  models.FloatField(blank=True, null=True, default=0)
   
   CASTE_CHOICES = [
        ('SC', 'Scheduled Caste (SC)'),
        ('ST', 'Scheduled Tribe (ST)'),
        ('OBC', 'Other Backward Class (OBC)'),
        ('General', 'General'),
        ('Prefer_not_to_say', 'Prefer not to say'),
        ('All', 'All'),
        ('NA', 'NA'),
    ]
   post_caste = models.CharField(max_length=20, choices=CASTE_CHOICES, blank=True, null=True, default="")
    
   RELIGION_CHOICES = [
        ('Hin', 'Hinduism'),
        ('Isl', 'Islam'),
        ('Chr', 'Christianity'),
        ('Sik', 'Sikhism'),
        ('Bud', 'Buddhism'),
        ('Jai', 'Jainism'),
        ('All', 'All'),
    ]
   post_religion = models.CharField(max_length=15, choices=RELIGION_CHOICES, blank=True, null=True, default="")
   
   DISABILITY_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('All', 'All'),
    ]
   post_has_disabilities = models.CharField(max_length=3, choices=DISABILITY_CHOICES, blank=True, null=True, default="")
   post_active = models.BooleanField(default=True)
   post_verified = models.BooleanField(default=False)
   post_read = models.BooleanField(default=False)
   post_create_date = models.DateTimeField(auto_now_add=True)
   post_start_date = models.DateField(blank=True, null=True, default=None)
   post_end_date = models.DateField(blank=True, null=True, default=None)

   def __str__(self):
       return f"{self.id}: {self.post_title}"
   
   
 
 
# ==========================================  
#              Post Category
# ==========================================   


class PostCategoryEducation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(WelfarePost, on_delete=models.CASCADE)
    current_school = models.CharField(max_length=255, blank=True, null=True, default=None)
    grade = models.CharField(max_length=255, blank=True, null=True, default=None)
    academic_performance = models.CharField(max_length=255, blank=True, null=True, default=None)
    reason_for_application = models.CharField(max_length=255, blank=True, null=True, default=None)
    is_applied = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    new_flag = models.BooleanField(default=True)
    submit_date = models.DateField(blank=True, null=True, default=None)
    
    def __str__(self):
       return f"{self.user.full_name} --- {self.post.post_category}--- {self.post.post_title} --- {self.is_applied}"
    
    
class PostCategoryHealth(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(WelfarePost, on_delete=models.CASCADE)
    
    city = models.CharField(max_length=255, blank=True, null=True, default=None)
    ration_card_no = models.CharField(max_length=255, blank=True, null=True, default=None)
    medical_history = models.CharField(max_length=255, blank=True, null=True, default=None)
    allergies = models.CharField(max_length=255, blank=True, null=True, default=None)
    height = models.CharField(max_length=255, blank=True, null=True, default=None)
    weight = models.CharField(max_length=255, blank=True, null=True, default=None)
    blood_pressure_condition = models.CharField(max_length=255, blank=True, null=True, default=None)
    blood_group = models.CharField(max_length=255, blank=True, null=True, default=None)
    vision_condition = models.CharField(max_length=255, blank=True, null=True, default=None)
    hearing_condition = models.CharField(max_length=255, blank=True, null=True, default=None)
    health_insurance = models.CharField(max_length=255, blank=True, null=True, default=None)
    govt_health_card = models.CharField(max_length=255, blank=True, null=True, default=None)

    is_applied = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    new_flag = models.BooleanField(default=True)
    submit_date = models.DateField(blank=True, null=True, default=None)
    
    def __str__(self):
       return f"{self.user.full_name} --- {self.post.post_title} --- {self.is_applied}"
    
    
class PostCategoryEmployment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(WelfarePost, on_delete=models.CASCADE)
    
    company_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    job_entry_date = models.DateField(blank=True, null=True, default=None)
    retirement_date = models.DateField(blank=True, null=True, default=None)
    job_post = models.CharField(max_length=255, blank=True, null=True, default=None)
    salary_per_month = models.CharField(max_length=255, blank=True, null=True, default=None)
    
    is_applied = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    new_flag = models.BooleanField(default=True)
    submit_date = models.DateField(blank=True, null=True, default=None)
    
    def __str__(self):
       return f"{self.user.full_name} --- {self.post.post_title} --- {self.is_applied}"
    
    
# Housing          
class PostCategoryHousing(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(WelfarePost, on_delete=models.CASCADE)
    
    ration_card_no = models.CharField(max_length=255, blank=True, null=True, default=None)
    land_area = models.CharField(max_length=255, blank=True, null=True, default=None)
    survey_no = models.CharField(max_length=255, blank=True, null=True, default=None)
    no_of_members = models.IntegerField(blank=True, null=True, default=0)
    location = models.CharField(max_length=255, blank=True, null=True, default=None)
    
    is_applied = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    new_flag = models.BooleanField(default=True)
    submit_date = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
       return f"{self.user.full_name} --- {self.post.post_title} --- {self.is_applied}"
   
   
# Rural_Development      
class PostCategoryRuralDevelopment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(WelfarePost, on_delete=models.CASCADE)
    
        
    is_applied = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    new_flag = models.BooleanField(default=True)
    submit_date = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
       return f"{self.user.full_name} --- {self.post.post_title} --- {self.is_applied}"
    
    
# Minority_Welfare      
class PostCategoryMinorityWelfare(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(WelfarePost, on_delete=models.CASCADE)
    
        
    is_applied = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    new_flag = models.BooleanField(default=True)
    submit_date = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
       return f"{self.user.full_name} --- {self.post.post_title} --- {self.is_applied}"
    


# Report An Issue

class ReportAnIssue(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True,)
    email = models.EmailField(blank=True, null=True,)
    issue_message = models.TextField(blank=True, null=True,)
    submit_date = models.DateTimeField(auto_now_add=True)
    issue_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.name
     
     
# Report An Issue

class AskQuery(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True,)
    email = models.EmailField(blank=True, null=True,)
    query_message = models.TextField(blank=True, null=True,)
    submit_date = models.DateTimeField(auto_now_add=True)
    query_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True,)
    email = models.EmailField(blank=True, null=True,)
    feedback_message = models.TextField(blank=True, null=True,)
    submit_date = models.DateTimeField(auto_now_add=True)
    feedback_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.name




# models.py
from django.conf import settings
from django.db import models

class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.description}'