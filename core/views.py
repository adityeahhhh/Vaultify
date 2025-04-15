# core/views.py

from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .models import Message
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import CapsuleForm,CustomUserCreationForm

# def register(request):
#     form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('login')
#     return render(request, 'core/register.html', {'form': form})

def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'core/register.html', {'form': form})

def main_page(request):
    return render(request, 'core/main.html')

@login_required
def create_capsule(request):
    form = CapsuleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        capsule = form.save(commit=False)
        capsule.user = request.user
        capsule.save()
        return redirect('your_capsules')
    return render(request, 'core/create_capsule.html', {'form': form})

@login_required
def public_messages(request):
    messages = Message.objects.filter(visibility='public', unlock_datetime__lte=timezone.now()).order_by('-unlock_datetime')
    return render(request, 'core/public.html', {'messages': messages})

@login_required
def your_capsules(request):
    messages = Message.objects.filter(user=request.user).order_by('-unlock_datetime')
    now = timezone.now()
    for msg in messages:
        remaining = (msg.unlock_datetime - now).total_seconds()
        msg.remaining = remaining if remaining > 0 else 0
    return render(request, 'core/your_capsules.html', {'messages': messages, 'now': now})

@login_required
def profile(request):
    return render(request, 'core/profile.html')
