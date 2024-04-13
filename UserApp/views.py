from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import models
from datetime import datetime, timedelta, time
from UserApp .models import CustomUser
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from AdminApp.models import WelfarePost, PostCategoryEducation, PostCategoryHealth, PostCategoryEmployment, PostCategoryMinorityWelfare, PostCategoryRuralDevelopment, PostCategoryHousing



# LOGIN & REGISTER

def LoginView(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
         login(request, user)
         if user.is_superuser:  
            return redirect('admin_dash') 
         else:
            return redirect('user_dash') 
      else:
         messages.error(request, 'Invalid username or password.')
         return redirect('login')
         
   context = {}
   html = 'UserApp/Login.html'
   return render(request, html, context)


def RegisterOneView(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        aadhar_no = request.POST.get('aadhar_no')
        
        try:
            user = models.CustomUser.objects.create_user(
                username = username, 
                email = email, 
                password = password, 
                aadhar_no = aadhar_no,
                )
            # Authenticate the user
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('register_two')
        except IntegrityError:
            error_message = "Error : Aadhar number already exists."
            return render(request, 'UserApp/Register-1.html',{'error_message': error_message})
                            
   return render(request, 'UserApp/Register-1.html')

 
@login_required(login_url='login') 
def RegisterTwoView(request):
   if request.method == 'POST':
      user = request.user
      user.username = request.POST.get('username')
      user.full_name = request.POST.get('full_name')
      user.profile_img = request.FILES.get('profile_img') 
      user.gender = request.POST.get('gender')
      user.age = request.POST.get('age')
      user.dob = request.POST.get('dob')
      user.email = request.POST.get('email')
      user.mobile_no = request.POST.get('mobile_no')
      user.address = request.POST.get('address')
      user.father = request.POST.get('father')
      user.mother = request.POST.get('mother')
      user.marital_status = request.POST.get('marital_status')
      user.children_no = request.POST.get('children_no')
      user.employment_status = request.POST.get('employment_status')
      user.occupation   = request.POST.get('occupation')
      user.monthly_income = request.POST.get('monthly_income')
      user.highest_education = request.POST.get('highest_education')
      user.highest_education_mark = request.POST.get('highest_education_mark')
      user.caste = request.POST.get('caste')
      user.religion = request.POST.get('religion')
      user.has_disabilities = request.POST.get('has_disabilities')
      user.disabilities_specify = request.POST.get('disabilities_specify')
      user.account_number = request.POST.get('account_number')
      user.bank_name = request.POST.get('bank_name')
      user.ifsc_code = request.POST.get('ifsc_code')
      user.aadhar_img = request.FILES.get('aadhar_img') 
      user.identity_img= request.FILES.get('identity_img') 
      user.verified_flag = 'False'
      user.profile_updated_flag = 'True'
      user.reg_date = datetime.today().date()
      user.save()
      return redirect('user_dash')
      
   context = {}
   html = 'UserApp/Register-2.html'
   return render(request, html, context)


@login_required(login_url='login') 
def MyProfileView(request):
   data = request.user
   context = {
      'data': data
   }
   html = 'UserApp/MyProfile.html'
   return render(request, html, context)


@login_required(login_url='login') 
def MyProfileUpdateView(request):
   data = request.user
   if request.method == 'POST':
      user = request.user
      user.username = request.POST.get('username')
      user.full_name = request.POST.get('full_name')
      user.gender = request.POST.get('gender')
      user.age = request.POST.get('age')
      user.dob = request.POST.get('dob')
      user.email = request.POST.get('email')
      user.mobile_no = request.POST.get('mobile_no')
      user.address = request.POST.get('address')
      user.father = request.POST.get('father')
      user.mother = request.POST.get('mother')
      user.marital_status = request.POST.get('marital_status')
      user.children_no = request.POST.get('children_no')
      user.employment_status = request.POST.get('employment_status')
      user.occupation   = request.POST.get('occupation')
      user.monthly_income = request.POST.get('monthly_income')
      user.highest_education = request.POST.get('highest_education')
      user.highest_education_mark = request.POST.get('highest_education_mark')
      user.caste = request.POST.get('caste')
      user.religion = request.POST.get('religion')
      user.has_disabilities = request.POST.get('has_disabilities')
      user.disabilities_specify = request.POST.get('disabilities_specify')
      user.account_number = request.POST.get('account_number')
      user.bank_name = request.POST.get('bank_name')
      user.ifsc_code = request.POST.get('ifsc_code')
      user.verified_flag = 'False'
      user.profile_updated_flag = 'True'
      user.reg_date = datetime.today().date()
      profile_img = request.FILES.get('profile_img') 
      aadhar_img = request.FILES.get('aadhar_img') 
      identity_img = request.FILES.get('identity_img') 
      user.verified_flag = 'False'
      
      if profile_img :
            user.profile_img = profile_img
            
      if aadhar_img :
            user.aadhar_img = aadhar_img
            
      if identity_img :
            user.identity_img = identity_img
            
      user.save()
      return redirect('user_dash')
      

   context = {
      'data': data
   }
   html = 'UserApp/MyProfile-Update.html'
   return render(request, html, context)


@login_required(login_url='login') 
def MyDocumentsView(request):
   data = request.user
   context = {
      'data': data
   }
   html = 'UserApp/MyDocuments.html'
   return render(request, html, context)


# ==================================
 
# ==================================





 

# USER DASHBOARD
 
@login_required(login_url='login')
def UserDashboardView(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.full_name = request.POST.get('full_name')
        user.profile_img = request.FILES.get('profile_img')
        user.gender = request.POST.get('gender')
        user.age = request.POST.get('age')
        user.dob = request.POST.get('dob')
        user.email = request.POST.get('email')
        user.mobile_no = request.POST.get('mobile_no')        
        user.father = request.POST.get('father')        
        user.mother = request.POST.get('mother')        
        user.marital_status = request.POST.get('marital_status')        
        user.children_no = request.POST.get('children_no')        
        user.employment_status = request.POST.get('employment_status')        
        user.occupation = request.POST.get('occupation')        
        user.monthly_income = request.POST.get('monthly_income')        
        user.highest_education = request.POST.get('highest_education')        
        user.highest_education_mark = request.POST.get('highest_education_mark')        
        user.caste = request.POST.get('caste')        
        user.religion = request.POST.get('religion')        
        user.has_disabilities = request.POST.get('has_disabilities')        
        user.disabilities_specify = request.POST.get('disabilities_specify')        
        user.account_number = request.POST.get('account_number')        
        user.bank_name = request.POST.get('bank_name')        
        user.ifsc_code = request.POST.get('ifsc_code')                
        user.aadhar_img = request.FILES.get('aadhar_img') 
        user.identity_img = request.FILES.get('identity_img') 
        user.profile_updated_flag = "True" 
        
        user.save()
        return redirect('user_dash')
    context = {}
    html = 'UserApp/User-Dashboard.html'
    return render(request, html, context)
 
 
 
# def HomeView(request):
#     notifications = [
#         {'id': 1, 'title': 'Lorem Ipsum', 'message': 'Quae dolorem earum veritatis odit seno', 'time': '30 min. ago'},
#         {'id': 2, 'title': 'Atque rerum nesciunt', 'message': 'Quae dolorem earum veritatis odit seno', 'time': '1 hr. ago'},
#         {'id': 3, 'title': 'Sit rerum fuga', 'message': 'Quae dolorem earum veritatis odit seno', 'time': '2 hrs. ago'},
#         {'id': 4, 'title': 'Dicta reprehenderit', 'message': 'Quae dolorem earum veritatis odit seno', 'time': '4 hrs. ago'},
#     ]
#     context = {
#         'notifications': notifications,
#     }
#     html = 'Home.html'
#     return render(request, html, context)
 

@login_required(login_url='login') 
def MyPostAllView(request):
    current_date = timezone.now().date()
    try:
        user_monthly_income = float(request.user.monthly_income)
    except ValueError:
        user_monthly_income = 0.0
        
    education_levels = {
         'NA' : 0,
        'All': 1,
        'Primary': 2,
        'Secondary': 3,
        'High': 4,
        'Dip': 5,
        'Bachelors': 6,
        'Masters': 7,
        'Doctorate': 8,
    }
    user_education_level = education_levels.get(request.user.highest_education, 0)
    eligible_education_levels = [level for level, value in education_levels.items() if value <= user_education_level]

    welfare_posts = WelfarePost.objects.filter(
        post_active=True,
        post_age__lte=request.user.age or 0,    
        post_gender__in=[request.user.gender, 'All'],
        post_marital_status__in=[request.user.marital_status, 'Both'],
        post_children__lte=request.user.children_no or 0,
        post_employment_status__in=[request.user.employment_status, 'All'],
        post_occupation__in=[request.user.occupation, 'All'],
        post_monthly_income__lte=user_monthly_income or 0.0,
        post_highest_education__in=eligible_education_levels + ['All'],
        post_caste__in=[request.user.caste, 'All'],
        post_religion__in=[request.user.religion, 'All'],
        post_has_disabilities__in=[request.user.has_disabilities, 'All'],
        post_end_date__gte=current_date,
    )
    

    context = {
       'post':welfare_posts,
    }
    html = 'UserApp/MyPost-All.html'
    return render(request, html, context)


@login_required(login_url='login') 
def MyPostThisMonthView(request):
   current_date = timezone.now().date()
   start_of_month = current_date.replace(day=1)
   end_of_month = start_of_month.replace(month=start_of_month.month % 12 + 1, day=1) - timedelta(days=1)

   try:
      user_monthly_income = float(request.user.monthly_income)
   except ValueError:
      user_monthly_income = 0.0
      
   education_levels = {
      'NA' : 0,
      'All': 1,
      'Primary': 2,
      'Secondary': 3,
      'High': 4,
      'Dip': 5,
      'Bachelors': 6,
      'Masters': 7,
      'Doctorate': 8,
   }
   user_education_level = education_levels.get(request.user.highest_education, 0)
   eligible_education_levels = [level for level, value in education_levels.items() if value <= user_education_level]
   
   welfare_posts_filter = {
      'post_active': True,
      'post_age__lte': request.user.age or 0,
      'post_gender__in': [request.user.gender, 'All'] if request.user.gender else ['All'],
      'post_marital_status__in': [request.user.marital_status, 'Both'] if request.user.marital_status else ['Both'],
      'post_children__lte': request.user.children_no or 0,
      'post_employment_status__in': [request.user.employment_status, 'All'] if request.user.employment_status else ['All'],
      'post_occupation__in': [request.user.occupation, 'All'] if request.user.occupation else ['All'],
      'post_monthly_income__lte': user_monthly_income or 0.0,
      'post_highest_education__in': eligible_education_levels + ['All'],
      'post_caste__in': [request.user.caste, 'All'] if request.user.caste else ['All'],
      'post_religion__in': [request.user.religion, 'All'] if request.user.religion else ['All'],
      'post_has_disabilities__in': [request.user.has_disabilities, 'All'] if request.user.has_disabilities else ['All'],
      'post_end_date__gte': current_date,
      'post_start_date__year': current_date.year,
      'post_start_date__month': current_date.month,
   }
   welfare_posts = WelfarePost.objects.filter(**welfare_posts_filter)
   
   today_date_ = datetime.now()
   this_month = today_date_.strftime('%B')
   this_year = current_date.year

   context = {
       'post':welfare_posts,
       'this_month':this_month,
       'this_year':this_year,
   }
   html = 'UserApp/MyPost-ThisMonth.html'
   return render(request, html, context)




def error_page(request):
    error_message = request.GET.get('error_message', 'An error occurred. Please try again later.')
    return render(request, 'UserApp/Error.html', {'error_message': error_message})




@login_required(login_url='login')
def MyPostApplyView(request, post_id):
    obj1 = get_object_or_404(WelfarePost, pk=post_id)
    post_category = obj1.post_category

    if request.method == 'POST' and post_category == 'Education':
        current_school = request.POST.get('current_school')
        grade = request.POST.get('grade')
        academic_performance = request.POST.get('academic_performance')
        reason_for_application = request.POST.get('reason_for_application')

        existing_application = PostCategoryEducation.objects.filter(user=request.user, post=obj1).exists()
        if existing_application:
            messages.error(request, 'You have already applied for this post.')
            return redirect('mypost_apply', post_id=post_id)

        obj = PostCategoryEducation(
            user=request.user,
            post=obj1,
            current_school=current_school,
            grade=grade,
            academic_performance=academic_performance,
            reason_for_application=reason_for_application,
            is_applied=True,
            is_approved=False,
            is_pending=True,
            is_rejected=False,
            new_flag=True,
            submit_date=datetime.today().date()
        )
        obj.save()
        return redirect('mypost_all')

    elif request.method == 'POST' and post_category == 'Healthcare':
        city = request.POST.get('city')
        ration_card_no = request.POST.get('ration_card_no')
        medical_history = request.POST.get('medical_history')
        allergies = request.POST.get('allergies')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        blood_pressure_condition = request.POST.get('blood_pressure_condition')
        blood_group = request.POST.get('blood_group')
        vision_condition = request.POST.get('vision_condition')
        hearing_condition = request.POST.get('hearing_condition')
        health_insurance = request.POST.get('health_insurance')
        govt_health_card = request.POST.get('govt_health_card')

        existing_application = PostCategoryHealth.objects.filter(user=request.user, post=obj1).exists()
        if existing_application:
            messages.error(request, 'You have already applied for this post.')
            return redirect('mypost_apply', post_id=post_id)

        obj = PostCategoryHealth(
            user=request.user,
            post=obj1,
            city=city,
            ration_card_no=ration_card_no,
            medical_history=medical_history,
            allergies=allergies,
            height=height,
            weight=weight,
            blood_pressure_condition=blood_pressure_condition,
            blood_group=blood_group,
            vision_condition=vision_condition,
            hearing_condition=hearing_condition,
            health_insurance=health_insurance,
            govt_health_card=govt_health_card,
            is_applied=True,
            is_approved=False,
            is_pending=True,
            is_rejected=False,
            new_flag=True,
            submit_date=datetime.today().date()
        )
        obj.save()
        return redirect('mypost_all')
     
    elif request.method == 'POST' and post_category == 'Employment':
        company_name = request.POST.get('company_name')
        job_entry_date = request.POST.get('job_entry_date')
        retirement_date = request.POST.get('retirement_date')
        job_post = request.POST.get('job_post')
        salary_per_month = request.POST.get('salary_per_month')
        
        existing_application = PostCategoryEmployment.objects.filter(user=request.user, post=obj1).exists()
        if existing_application:
            messages.error(request, 'You have already applied for this post.')
            return redirect('mypost_apply', post_id=post_id)

        obj = PostCategoryEmployment(
            user=request.user,
            post=obj1,
            company_name=company_name,
            job_entry_date=job_entry_date,
            retirement_date=retirement_date,
            job_post=job_post,
            salary_per_month=salary_per_month,
            is_applied=True,
            is_approved=False,
            is_pending=True,
            is_rejected=False,
            new_flag=True,
            submit_date=datetime.today().date()
        )
        obj.save()
        return redirect('mypost_all')
    
    elif request.method == 'POST' and post_category == 'Housing':
        # company_name = request.POST.get('company_name')
        
        existing_application = PostCategoryHousing.objects.filter(user=request.user, post=obj1).exists()
        if existing_application:
            messages.error(request, 'You have already applied for this post.')
            return redirect('mypost_apply', post_id=post_id)

        obj = PostCategoryHousing(
            user=request.user,
            post=obj1,
            
            # company_name=company_name,
            
            is_applied=True,
            is_approved=False,
            is_pending=True,
            is_rejected=False,
            new_flag=True,
            submit_date=datetime.today().date()
        )
        obj.save()
        return redirect('mypost_all')
    
    elif request.method == 'POST' and post_category == 'Rural_Development':
        # company_name = request.POST.get('company_name')
        
        existing_application = PostCategoryRuralDevelopment.objects.filter(user=request.user, post=obj1).exists()
        if existing_application:
            messages.error(request, 'You have already applied for this post.')
            return redirect('mypost_apply', post_id=post_id)

        obj = PostCategoryRuralDevelopment(
            user=request.user,
            post=obj1,
            
            # company_name=company_name,
            
            is_applied=True,
            is_approved=False,
            is_pending=True,
            is_rejected=False,
            new_flag=True,
            submit_date=datetime.today().date()
        )
        obj.save()
        return redirect('mypost_all')
    
    elif request.method == 'POST' and post_category == 'Minority_Welfare':
        # company_name = request.POST.get('company_name')
        
        existing_application = PostCategoryMinorityWelfare.objects.filter(user=request.user, post=obj1).exists()
        if existing_application:
            messages.error(request, 'You have already applied for this post.')
            return redirect('mypost_apply', post_id=post_id)

        obj = PostCategoryMinorityWelfare(
            user=request.user,
            post=obj1,
            
            # company_name=company_name,
            
            is_applied=True,
            is_approved=False,
            is_pending=True,
            is_rejected=False,
            new_flag=True,
            submit_date=datetime.today().date()
        )
        obj.save()
        return redirect('mypost_all')
    
    context = {
        'data': obj1
    }
    return render(request, 'UserApp/MyPost-Apply.html', context)





# Report An Issue

from AdminApp.models import ReportAnIssue, AskQuery

def ReportIssueView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        issue_message = request.POST.get('issue_message')

        ReportAnIssue.objects.create(
           name=name, 
           email=email, 
           issue_message=issue_message, 
           issue_flag=True
           )
        if request.user.is_authenticated:
            return redirect('user_dash')
        else:
            return redirect('login')
   
    return render(request, 'UserApp/Report-Issue.html')


# Ask Query

def AskQueryView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query_message = request.POST.get('query_message')

        AskQuery.objects.create(
           name=name, 
           email=email, 
           query_message=query_message, 
           query_flag=True
           )
        if request.user.is_authenticated:
            return redirect('user_dash')
        else:
            return redirect('login')
   
    return render(request, 'UserApp/Ask-Query.html')