from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, ProfileForm
from .models import Profile
from django.contrib.auth.decorators import user_passes_test

def home(request):
    return render(request, 'home.html', {})
# Register view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        weight = request.POST['weight']
        height = request.POST['height']
        region = request.POST['region']
        province = request.POST['province']
        municipality = request.POST['municipality']
        blood_type = models.CharField(max_length=3, choices=[
            ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
            ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
        ])
        availability = models.BooleanField(default=True)

        user = User.objects.create_user(username=username, email=email, password=password,
                                        first_name=first_name, last_name=last_name)
        Profile.objects.create(user=user, weight=weight, height=height, region=region,
                               province=province, municipality=municipality, blood_type=blood_type,
                               availability=availability)

        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')

    return render(request, 'register.html')


# Profile creation view
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'donors/../templates/profile_create.html', {'form': form})

# Profile view
from django.contrib.auth.decorators import login_required

@login_required  # Ensure only logged-in users can access this view
def profile_view(request):
    user = request.user
    # Here, you can retrieve the user's profile information if you have a Profile model
    return render(request, 'profile.html', {'user': user})

# Custom login view
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not Profile.objects.filter(user=user).exists():
                return redirect('profile_create')
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'donors/../templates/login.html', {'form': form})

# donors/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# donors/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile  # Adjust this import based on your Profile model's location

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user has a profile
            if Profile.objects.filter(user=user).exists():
                login(request, user)
                return redirect('home')  # Redirect to homepage if profile exists
            else:
                return redirect('profile_create')  # Redirect to profile creation if no profile
        else:
            # Invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    # Ensure we always return an HttpResponse for GET requests
    return render(request, 'login.html')
