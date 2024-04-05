# User

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('login/', views.LoginView, name='login'),
   path('register_one/', views.RegisterOneView, name='register_one'),
   path('register_two/', views.RegisterTwoView, name='register_two'),
   path('my_profile/', views.MyProfileView, name='my_profile'),
   path('my_profile_update/', views.MyProfileUpdateView, name='my_profile_update'),
   path('my_documents/', views.MyDocumentsView, name='my_documents'),
   
   path('', views.UserDashboardView, name='user_dash'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
   path('mypost_all/', views.MyPostAllView, name='mypost_all'),
   path('mypost_apply/<int:post_id>', views.MyPostApplyView, name='mypost_apply'),
   path('mypost_this_month/', views.MyPostThisMonthView, name='mypost_this_month'),
   
   path('error/', views.error_page, name='error_page'),
]
