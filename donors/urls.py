# donors/urls.py
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import home, register, login_view, profile_create, profile_view  # Import the views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home view
    path('register/', register, name='register'),  # Register view
    path('login/', login_view, name='login'),  # Login view
    path('profile/create/', profile_create, name='profile_create'),  # Profile creation view
    path('profile/', profile_view, name='profile'),  # Profile view
    path('admin-dashboard/', login_required(views.admin_dashboard), name='admin_dashboard'),
    path('admin-dashboard/create/', views.create_blood_donation_request, name='create_blood_donation_request'),
    path('admin-dashboard/edit/<int:pk>/', views.edit_blood_donation_request, name='edit_blood_donation_request'),
    path('admin-dashboard/delete/<int:pk>/', views.delete_blood_donation_request, name='delete_blood_donation_request'),
    path('admin-dashboard/edit-user/<int:pk>/', views.edit_user, name='edit_user'),
    path('admin-dashboard/delete-user/<int:pk>/', views.delete_user, name='delete_user'),
]