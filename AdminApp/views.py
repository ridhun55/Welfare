from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from UserApp .models import CustomUser
from AdminApp .models import WelfarePost, PostCategoryEducation
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime, date
from django.http import HttpResponseBadRequest




@login_required(login_url='login')
def AdminDashboardView(request):
    latest_5_post = WelfarePost.objects.order_by('-post_create_date')[:10]
    context = {
        'latest_5_post' : latest_5_post,
    }
    html = 'AdminApp/Admin-Dashboard.html'
    return render(request, html, context)


@login_required(login_url='login')
def UserProfileAllView(request):
    data = CustomUser.objects.all().order_by('-id')
    context = {
        'data' : data,
    }
    html = 'AdminApp/UserProfile-All.html'
    return render(request, html, context)


@login_required(login_url='login')
def UserProfileVerifiedView(request):
    data = CustomUser.objects.filter(verified_flag=True).order_by('-id')
    context = {
        'data' : data,
    }
    html = 'AdminApp/UserProfile-Verified.html'
    return render(request, html, context)


@login_required(login_url='login')
def UserProfileVerifyPendingView(request):
    data = CustomUser.objects.filter(verified_flag=False).order_by('-id')
    context = {
        'data' : data,
    }
    html = 'AdminApp/UserProfile-Verify-Pending.html'
    return render(request, html, context)


@login_required(login_url='login')
def UserProfileView(request, id):
    data = CustomUser.objects.get(id=id)  # Assuming CustomUser model has a 'user' field
    if request.method == 'POST':
        obj = CustomUser.objects.get(id=id)
        verified_flag = request.POST.get('verified_flag') 
        if verified_flag :
            obj.verified_flag = verified_flag
        
        obj.save()
        return redirect('user_profile_All')
        
    context = {
        'data' : data,
    }
    html = 'AdminApp/UserProfile-View.html'
    return render(request, html, context)


@login_required(login_url='login')
def UserProfileDeleteView(request, pk):
    userprofile = get_object_or_404(CustomUser, pk=pk)
    userprofile.delete()
    return redirect('user_profile_All')  # Redirect to the model changelist




# Welfare Post

@login_required(login_url='login')
def PostCreateView(request):
    data = WelfarePost.objects.all()
    if request.method == 'POST':   
        post_title = request.POST.get('post_title')
        post_description = request.POST.get('post_description')
        post_category = request.POST.get('post_category')
        post_age = request.POST.get('post_age', '0')
        post_gender = request.POST.get('post_gender')
        post_marital_status = request.POST.get('post_marital_status')
        post_children = request.POST.get('post_children')
        post_employment_status = request.POST.get('post_employment_status')
        post_occupation = request.POST.get('post_occupation')
        post_monthly_income = request.POST.get('post_monthly_income')
        post_highest_education = request.POST.get('post_highest_education')
        post_highest_education_mark = request.POST.get('post_highest_education_mark')
        post_caste = request.POST.get('post_caste')
        post_religion = request.POST.get('post_religion')
        post_has_disabilities = request.POST.get('post_has_disabilities')
        post_img = request.FILES.get('post_img') 
        post_create_date = datetime.today().date()
        post_start_date = request.POST.get('post_start_date')
        post_end_date = request.POST.get('post_end_date')
        
        start_date = datetime.strptime(post_start_date, '%Y-%m-%d')
        end_date = datetime.strptime(post_end_date, '%Y-%m-%d')

        if start_date > end_date:
            messages.error(request, "Start date cannot be greater than end date")
            return redirect('post_create') 
 
        obj = WelfarePost.objects.create(
            post_title=post_title,
            post_description=post_description,
            post_category=post_category,
            post_gender=post_gender,
            post_marital_status=post_marital_status,
            post_employment_status=post_employment_status,
            post_occupation=post_occupation,
            post_highest_education=post_highest_education,
            post_caste=post_caste,
            post_religion=post_religion,
            post_has_disabilities=post_has_disabilities,
            post_active=True,
            post_verified=False,
            post_read=False,
            post_create_date=post_create_date,
            post_start_date=post_start_date,
            post_end_date=post_end_date,
        )
            
        if post_img:
            obj.post_img = post_img
        
        if post_age:
            obj.post_age = post_age
        else:
            obj.post_age = 0
            
        if post_children:
            obj.post_children = post_children
        else:
            obj.post_children = 0
            
        if post_monthly_income:
            obj.post_monthly_income = post_monthly_income
        else:
            obj.post_monthly_income = 0
            
        if post_highest_education_mark:
            obj.post_highest_education_mark = post_highest_education_mark
        else:
            obj.post_highest_education_mark = 0

        obj.save()
        messages.success(request, "Post created successfully")
        return redirect('post_all')  # Redirect to a list of posts after creating the post
      
    context = {
        'data' : data,
    }
    html = 'AdminApp/Post-Create.html'
    return render(request, html, context)


@login_required(login_url='login')
def PostUpdateView(request, pk):
    data = WelfarePost.objects.get(id=pk)
    if request.method == 'POST':
        post_title = request.POST.get('post_title')
        post_description = request.POST.get('post_description')
        post_category = request.POST.get('post_category')
        post_age = request.POST.get('post_age')    
        post_gender = request.POST.get('post_gender')
        post_marital_status = request.POST.get('post_marital_status')
        post_children = request.POST.get('post_children')
        post_employment_status = request.POST.get('post_employment_status')
        post_occupation = request.POST.get('post_occupation')
        post_monthly_income = request.POST.get('post_monthly_income')
        post_highest_education = request.POST.get('post_highest_education')
        post_highest_education_mark = request.POST.get('post_highest_education_mark')
        post_caste = request.POST.get('post_caste')
        post_religion = request.POST.get('post_religion')
        post_has_disabilities = request.POST.get('post_has_disabilities')
        post_start_date = request.POST.get('post_start_date')
        post_end_date = request.POST.get('post_end_date')
        post_active = request.POST.get('post_active')
        start_date = datetime.strptime(post_start_date, '%Y-%m-%d')
        end_date = datetime.strptime(post_end_date, '%Y-%m-%d')
        post_img = request.FILES.get('post_img')

        obj = WelfarePost.objects.get(id=pk)
        if post_active:
            obj.post_active = post_active

        obj.post_title = post_title
        obj.post_description = post_description
        obj.post_category = post_category
        obj.post_gender = post_gender
        obj.post_marital_status = post_marital_status
        obj.post_employment_status = post_employment_status
        obj.post_occupation = post_occupation
        obj.post_highest_education = post_highest_education
        obj.post_caste = post_caste
        obj.post_religion = post_religion
        obj.post_has_disabilities = post_has_disabilities
        obj.post_start_date = post_start_date
        obj.post_end_date = post_end_date
        
        
        if post_img:
            obj.post_img = post_img
        
        if post_age:
            obj.post_age = post_age
        else:
            obj.post_age = 0
            
        if post_children:
            obj.post_children = post_children
        else:
            obj.post_children = 0
            
        if post_monthly_income:
            obj.post_monthly_income = post_monthly_income
        else:
            obj.post_monthly_income = 0
            
        if post_highest_education_mark:
            obj.post_highest_education_mark = post_highest_education_mark
        else:
            obj.post_highest_education_mark = 0

        if start_date > end_date:
            messages.error(request, "Start date cannot be greater than end date")
            return redirect('post_all')
        else:
            obj.save()
            messages.success(request, "Post Updated")
            return redirect('post_all')

    context = {
        'post': data,
    }
    html = 'AdminApp/Post-Update.html'
    return render(request, html, context)


@login_required(login_url='login')
def PostReadView(request, pk):
    post = get_object_or_404(WelfarePost, id=pk)
    context = {
        'post': post,
    }
    return render(request, 'AdminApp/Post-Read.html', context)


@login_required(login_url='login')
def PostActiveView(request):
    today_date = date.today()
    data = WelfarePost.objects.filter(post_end_date__gte=today_date, post_active=True)
    context = {
        'data' : data,
        'today_date':date.today()
    }
    html = 'AdminApp/Post-Active.html'
    return render(request, html, context)


@login_required(login_url='login')
def PostOutdatedView(request):
    today_date = date.today()
    outdated_post = WelfarePost.objects.filter(post_end_date__lt=today_date)
    context = {
        'data': outdated_post,
        'today_date':date.today()
    }
    return render(request, 'AdminApp/Post-Outdated.html', context)



   # ===================

# @login_required(login_url='login')
# def PostAllView(request):
#     data = WelfarePost.objects.all().order_by('-id')
#     context = {
#         'data': data,
#         'today_date':date.today()
#     }
#     return render(request, 'AdminApp/Post-All.html', context)

    
    
def PostAllView(request):
    today_date = date.today()
    WelfarePost.objects.filter(post_end_date__lt=today_date).update(post_active=False)

    data = WelfarePost.objects.all().order_by('-id')

    context = {
        'data': data,
        'today_date': today_date
    }
    return render(request, 'AdminApp/Post-All.html', context)
    
    # ===================


@login_required(login_url='login')
def PostDeleteView(request, pk):
    obj2 = get_object_or_404(WelfarePost, pk=pk)
    obj2.delete()
    messages.success(request, f"Post ID {pk} has been deleted.")
    return redirect('post_all')





# Verify Application

@login_required(login_url='login')
def PostVerifyAllView(request):
    data_education = WelfarePost.objects.filter(
        postcategoryeducation__is_applied=True,
        postcategoryeducation__is_pending=True
    ).distinct()
    
    data_health = WelfarePost.objects.filter(
        postcategoryhealth__is_applied=True,
        postcategoryhealth__is_pending=True
    ).distinct()
    
    data_employment = WelfarePost.objects.filter(
        postcategoryemployment__is_applied=True,
        postcategoryemployment__is_pending=True
    ).distinct()
    
    data_housing = WelfarePost.objects.filter(
        postcategoryhousing__is_applied=True,
        postcategoryhousing__is_pending=True
    ).distinct()
    
    data_rural_development = WelfarePost.objects.filter(
        postcategoryruraldevelopment__is_applied=True,
        postcategoryruraldevelopment__is_pending=True
    ).distinct()
    
    data_minority_welfare = WelfarePost.objects.filter(
        postcategoryminoritywelfare__is_applied=True,
        postcategoryminoritywelfare__is_pending=True
    ).distinct()

    
    context = {
        'data_education': data_education,
        'data_health': data_health,
        'data_employment': data_employment,
        'data_housing': data_housing,
        'data_rural_development': data_rural_development,
        'data_minority_welfare': data_minority_welfare,
    }
    return render(request, 'AdminApp/PostVerify-All.html', context)


@login_required(login_url='login')
def PostVerifyPendingView(request):
    data_education = WelfarePost.objects.filter(
        postcategoryeducation__is_applied=True,
        postcategoryeducation__is_pending=True,
        postcategoryeducation__is_approved=False
    ).distinct()
    
    data_health = WelfarePost.objects.filter(
        postcategoryhealth__is_applied=True,
        postcategoryhealth__is_pending=True,
        postcategoryhealth__is_approved=False  # Change to False
    ).distinct()
    
    data_employment = WelfarePost.objects.filter(
        postcategoryemployment__is_applied=True,
        postcategoryemployment__is_pending=True,
        postcategoryemployment__is_approved=False
    ).distinct()
    
    data_housing = WelfarePost.objects.filter(
        postcategoryhousing__is_applied=True,
        postcategoryhousing__is_pending=True,
        postcategoryhousing__is_approved=False
    ).distinct()
    
    data_rural_development = WelfarePost.objects.filter(
        postcategoryruraldevelopment__is_applied=True,
        postcategoryruraldevelopment__is_pending=True,
        postcategoryruraldevelopment__is_approved=False
    ).distinct()
    
    data_minority_welfare = WelfarePost.objects.filter(
        postcategoryminoritywelfare__is_applied=True,
        postcategoryminoritywelfare__is_pending=True,
        postcategoryminoritywelfare__is_approved=False
    ).distinct()
       
    combined_posts = chain(data_education, data_health, data_employment, data_housing, data_rural_development, data_minority_welfare)

    context = {
        'data_education': data_education,
        'data_health': data_health,
        'data_employment': data_employment,
        'data_housing': data_housing,
        'data_rural_development': data_rural_development,
        'data_minority_welfare': data_minority_welfare,
        'combined_data': combined_posts
    }
    return render(request, 'AdminApp/PostVerify-Pending.html', context)


@login_required(login_url='login')
def PostVerifyApprovedView(request):
    data_education = WelfarePost.objects.filter(
        postcategoryeducation__is_applied=True,
        postcategoryeducation__is_pending=True,
        postcategoryeducation__is_approved=True
    ).distinct()
    
    data_health = WelfarePost.objects.filter(
        postcategoryhealth__is_applied=True,
        postcategoryhealth__is_pending=True,
        postcategoryhealth__is_approved=True
    ).distinct()
    
    data_employment = WelfarePost.objects.filter(
        postcategoryemployment__is_applied=True,
        postcategoryemployment__is_pending=True,
        postcategoryemployment__is_approved=True
    ).distinct()
    
    data_housing = WelfarePost.objects.filter(
        postcategoryhousing__is_applied=True,
        postcategoryhousing__is_pending=True,
        postcategoryhousing__is_approved=True
    ).distinct()
    
    data_rural_development = WelfarePost.objects.filter(
        postcategoryruraldevelopment__is_applied=True,
        postcategoryruraldevelopment__is_pending=True,
        postcategoryruraldevelopment__is_approved=True
    ).distinct()
    
    data_minority_welfare = WelfarePost.objects.filter(
        postcategoryminoritywelfare__is_applied=True,
        postcategoryminoritywelfare__is_pending=True,
        postcategoryminoritywelfare__is_approved=True
    ).distinct()
    
    combined_posts = chain(data_education, data_health, data_employment, data_housing, data_rural_development, data_minority_welfare)


    context = {
        'data_education': data_education,
        'data_health': data_health,
        'data_employment': data_employment,
        'data_housing': data_housing,
        'data_rural_development': data_rural_development,
        'data_minority_welfare': data_minority_welfare,
        'combined_data': combined_posts
    }
    return render(request, 'AdminApp/PostVerify-Approved.html', context)


from itertools import chain
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import PostCategoryEducation, PostCategoryHealth, PostCategoryHousing, PostCategoryEmployment, PostCategoryRuralDevelopment, PostCategoryMinorityWelfare

@login_required(login_url='login')
def PostVerifyViewView(request, item_id, user_id):
    data_education = PostCategoryEducation.objects.filter(
        user_id=user_id,
        post_id=item_id,
    )
    data_health = PostCategoryHealth.objects.filter(
        user_id=user_id,
        post_id=item_id,
    )
    data_employment = PostCategoryEmployment.objects.filter(
        user_id=user_id,
        post_id=item_id,
    )
    data_housing = PostCategoryHousing.objects.filter(
        user_id=user_id,
        post_id=item_id,
    )
    data_rural_development = PostCategoryRuralDevelopment.objects.filter(
        user_id=user_id,
        post_id=item_id,
    )
    data_minority_welfare = PostCategoryMinorityWelfare.objects.filter(
        user_id=user_id,
        post_id=item_id,
    )

    # Update new_flag for PostCategoryEducation objects
    for post_education in data_education:
        if post_education.new_flag:
            post_education.new_flag = False
            post_education.save()

    # Update new_flag for PostCategoryHealth objects
    for post_health in data_health:
        if post_health.new_flag:
            post_health.new_flag = False
            post_health.save()

    # Update new_flag for PostCategoryEmployment objects
    for post_employment in data_employment:
        if post_employment.new_flag:
            post_employment.new_flag = False
            post_employment.save()
            
    # Update new_flag for PostCategoryHousing objects
    for post_housing in data_housing:
        if post_housing.new_flag:
            post_housing.new_flag = False
            post_housing.save()
            
    # Update new_flag for PostCategoryRuralDevelopment objects
    for post_rural_development in data_rural_development:
        if post_rural_development.new_flag:
            post_rural_development.new_flag = False
            post_rural_development.save()
            
    # Update new_flag for PostCategoryMinorityWelfare objects
    for post_minority_welfare in data_minority_welfare:
        if post_minority_welfare.new_flag:
            post_minority_welfare.new_flag = False
            post_minority_welfare.save()

    combined_posts = chain(data_education, data_health, data_employment, data_housing, data_rural_development, data_minority_welfare )

    # Form submission for updating approval status
    if request.method == 'POST':
        for post in combined_posts:
            if post.post.post_category == 'Education':
                is_approved = request.POST.get('is_approved')
                post.is_approved = is_approved == 'True'
                post.save()
            elif post.post.post_category == 'Healthcare':
                is_approved = request.POST.get('is_approved')
                post.is_approved = is_approved == 'True'
                post.save()
            elif post.post.post_category == 'Employment':
                is_approved = request.POST.get('is_approved')
                post.is_approved = is_approved == 'True'
                post.save()
            elif post.post.post_category == 'Housing':
                is_approved = request.POST.get('is_approved')
                post.is_approved = is_approved == 'True'
                post.save()
            elif post.post.post_category == 'Rural_Development':
                is_approved = request.POST.get('is_approved')
                post.is_approved = is_approved == 'True'
                post.save()
            elif post.post.post_category == 'Minority_Welfare':
                is_approved = request.POST.get('is_approved')
                post.is_approved = is_approved == 'True'
                post.save()

        # Redirect to a different view or URL after processing the form data
        return redirect('post_verify_all')

    context = {
        'data_education': data_education,
        'data_health': data_health,
        'data_employment': data_employment,
        'data_housing': data_housing,
        'data_rural_development': data_rural_development,
        'data_minority_welfare': data_minority_welfare,
        'combined_data': combined_posts
    }
    return render(request, 'AdminApp/PostVerify-View.html', context)




# IssueView
from AdminApp.models import ReportAnIssue, AskQuery

@login_required(login_url='login')
def IssueView(request):
    data = ReportAnIssue.objects.all().order_by('-id')
    context = {
        'data':data
    }
    return render(request, 'AdminApp/Issue.html', context)


@login_required(login_url='login')
def IssueReadView(request,id):
    data = ReportAnIssue.objects.get(id=id)
    context = {
        'data':data
    }
    return render(request, 'AdminApp/Issue-Read.html', context)


@login_required(login_url='login')
def IssueDeleteView(request, pk):
    obj = get_object_or_404(ReportAnIssue, pk=pk)
    obj.delete()
    messages.success(request, f"Issue ID {pk} has been deleted.")
    return redirect('issue') 

# QueryView

@login_required(login_url='login')
def QueryView(request):
    data = AskQuery.objects.all()
    context = {
        'data':data
    }
    return render(request, 'AdminApp/Query.html', context)


@login_required(login_url='login')
def QueryReadView(request,id):
    data = AskQuery.objects.get(id=id)
    context = {
        'data':data
    }
    return render(request, 'AdminApp/Query-Read.html', context)


@login_required(login_url='login')
def QueryDeleteView(request, pk):
    obj = get_object_or_404(AskQuery, pk=pk)
    obj.delete()
    messages.success(request, f"Query ID {pk} has been deleted.")
    return redirect('query') 



