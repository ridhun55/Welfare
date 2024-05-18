# Admin

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.AdminDashboardView, name='admin_dash'),
   path('user_profile_All/', views.UserProfileAllView, name='user_profile_All'),
   path('user_profile_verified/', views.UserProfileVerifiedView, name='user_profile_verified'),
   path('user_profile_verify_pending/', views.UserProfileVerifyPendingView, name='user_profile_verify_pending'),
   path('user_profile_view/<int:id>/view', views.UserProfileView, name='user_profile_view'),
   path('user_profile_delete/<int:pk>', views.UserProfileDeleteView, name='user_profile_delete'),
   
   path('post_create/', views.PostCreateView, name='post_create'),
   path('post_read/<int:pk>/', views.PostReadView, name='post_read'),
   path('post_update/<int:pk>/', views.PostUpdateView, name='post_update'),
   path('post_all/', views.PostAllView, name='post_all'),
   path('post_active/', views.PostActiveView, name='post_active'),
   path('post_outdated/', views.PostOutdatedView, name='post_outdated'),
   path('post_delete/<int:pk>/', views.PostDeleteView, name='post_delete'),
   
   path('post_verify_all/', views.PostVerifyAllView, name='post_verify_all'),
   path('post_verify_pending/', views.PostVerifyPendingView, name='post_verify_pending'),
   path('post_verify_approved/', views.PostVerifyApprovedView, name='post_verify_approved'),
   path('post_verify_view/<int:item_id>/<int:user_id>', views.PostVerifyViewView, name='post_verify_view'),
   
   path('issue', views.IssueView, name='issue'),
   path('issue_read/<int:id>', views.IssueReadView, name='issue_read'),
   path('issue_delete/<int:pk>', views.IssueDeleteView, name='issue_delete'),
   
   path('query', views.QueryView, name='query'),
   path('query_read/<int:id>', views.QueryReadView, name='query_read'),
   path('query_delete/<int:pk>', views.QueryDeleteView, name='query_delete'),

   path('feedback', views.FeedbackView, name='feedback'),
   path('feedback_read/<int:id>', views.FeedbackReadView, name='feedback_read'),
   path('feedback_delete/<int:id>', views.FeedbackDeleteView, name='feedback_delete'),
]