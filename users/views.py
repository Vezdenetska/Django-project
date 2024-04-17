from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm, UserChangePasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Uzytkownik {username} został zarejestrowany!')
            return redirect('profile')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Strona rejestracji',
            'form': form
        }
    )


@login_required
def profile(request):
    if request.method == "POST":
        profileForm = ProfileImageForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
            )
        updateUserForm = UserUpdateForm(
            request.POST,
            instance=request.user
            )
        
        if updateUserForm.is_valid() and profileForm.is_valid():
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Pomyślnie zaktualizowano dane w profilu osobistym!')
            return redirect('profile')

    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)
        
    
    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
    }

    return render(request, 'users/cabin.html', data)


def password(request):
    if request.method == "POST":
        updatePassword = UserChangePasswordForm(request.user, request.POST)
        if updatePassword.is_valid():
            user = updatePassword.save()
            # Aktualizuj sesję użytkownika, aby zachować go zalogowanym
            update_session_auth_hash(request, user)
            messages.success(request, f'Pomyślnie zaktualizowano hasło!')
            return redirect('profile')
    else:
        updatePassword = UserChangePasswordForm(request.user)

    data = {
        'updatePassword': updatePassword,
    }

    return render(request, 'users/cabin.html', data)
