from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserRegisterBio
from django.contrib.auth.decorators import login_required


# Types of messages: messages.debug,messages.info, messages.success, messages.warning, messages.error
def register(request):
    if request.method == 'POST':
        p_form = UserRegisterBio(request.POST)
        u_form = UserRegisterForm(request.POST)
        print(p_form)
        if u_form.is_valid(): #and p_form.is_valid():
            u_form.save()
            p_form.save(commite=False)
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        p_form = UserRegisterBio()
        u_form = UserRegisterForm()

    context ={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context ={
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)