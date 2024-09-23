# blood_donation_project/urls.py
from django.contrib import admin
from django.urls import path
from donors.views import home, register, login_view, profile_create, profile_view  # Ensure all views are imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # This should match the root URL
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/create/', profile_create, name='profile_create'),
    path('profile/', profile_view, name='profile'),
]
