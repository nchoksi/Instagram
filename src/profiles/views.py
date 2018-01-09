from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from images.models import Image
from .forms import UserEditForm, ProfileEditForm


# Create your views here.

@login_required
def dashboard(request):
    user = request.user
    images = Image.objects.filter(user=user)
    return render(request, 'profile/dashboard.html', {'section': 'dashboard', 'user': user, 'images': images})


@login_required
def edit(request):
    if request.method == 'POST':
        print("inside post")
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST or None, files=request.FILES or
                                                                                             None)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print('Successful')
        else:
            print('Failed')
        return render(request, 'profile/dashboard.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        print("inside get")
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'profile/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required()
def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)
