# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserImageForm
from .models import Blog, UserInformation
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .models import Blog, UserInformation


# Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create default UserInformation for the new user
            UserInformation.objects.create(user=user)

            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            # Invalid login, display an error message
            return render(request, 'accounts/login.html', {'error': 'Invalid login credentials'})

    return render(request, 'accounts/login.html')

# Home Page View (allows user to change profile image)
def home(request):
    if request.user.is_authenticated:
        user_info = UserInformation.objects.get(user=request.user)

        if request.method == 'POST' and 'image' in request.FILES:
            image_form = UserImageForm(request.POST, request.FILES, instance=user_info)
            if image_form.is_valid():
                image_form.save()
                return redirect('home')  # Reload the page after image update
        else:
            image_form = UserImageForm(instance=user_info)

        return render(request, 'accounts/home.html', {'image_form': image_form, 'user_info': user_info})

    return redirect('login')  # Redirect to login page if not authenticated
# accounts/views.py


def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page after logout





# View for the home page displaying blogs
@login_required
def home(request):
    user_info = UserInformation.objects.get(user=request.user)
    blogs = Blog.objects.all()  # Fetch blogs of all users, not just the logged-in user
    return render(request, 'accounts/home.html', {'user_info': user_info, 'blogs': blogs})

# View for adding a new blog
@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.user = request.user  # Automatically assign the logged-in user as the blog creator
            new_blog.save()
            return redirect('home')  # Redirect to the home page after blog creation
    else:
        form = BlogForm()
       
    return render(request, 'accounts/add_blog.html', {'form': form})