from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterForm, UpdateProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blogapp.models import Blog

# Create your views here.
def signup(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('index')

    context = {"form": form}
    return render(request, "core/signup.html", context)

def signin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.warning(request, "Invalid credentials")
            redirect("signin")
    context = {}
    return render(request, "core/login.html", context)

def signout(request):
    logout(request)
    return redirect("index")

@login_required(login_url="signin")
def profile(request):
    user = request.user
    blogs = Blog.objects.filter(user=user)
    context = {"user": user,
               "blogs": blogs,
               "is_own_profile": True,}
    return render(request, 'core/profile.html', context)

@login_required(login_url="signin")
def update_profile(request):
    if request.user.is_authenticated:
        user = request.user
        form = UpdateProfileForm(instance=user)
        if request.method == "POST":
            form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully")
                return redirect("profile")

    context = {"form": form}
    return render(request, 'core/update_profile.html', context)

User = get_user_model()

@login_required(login_url="signin")
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    blogs = Blog.objects.filter(user=user)

    is_following = False
    if request.user != user:
        is_following = user.followers.filter(id=request.user.id).exists()

    is_own_profile = True
    if request.user != user:
        is_own_profile = False
    context = {
        "user": user,
        "blogs": blogs,
        "is_following": is_following,
        "is_own_profile": is_own_profile,
    }
    return render(request, "core/profile.html", context)

@login_required(login_url="signin")
def follow_user(request, username):
    profile_user = get_object_or_404(User, username=username)

    if request.user != profile_user:
        if profile_user.followers.filter(id=request.user.id).exists():
            profile_user.followers.remove(request.user)
        else:
            profile_user.followers.add(request.user)

    return redirect('user_profile', username=username)


