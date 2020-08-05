from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from acc_app.forms import UserForm, UserProfileInfoForm
from acc_app.models import UserProfileInfo, User
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from collections import OrderedDict


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            user_name = user_form.cleaned_data.get('username')
            messages.success(
                request, user_name + ' Regitered successfully, Please contact the Admin for confirmation')
            registered = True
            return redirect('/')
        else:
            messages.error(request, user_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    context = {'user_form': user_form,
               'profile_form': profile_form,
               'registered': registered}
    return render(request, 'account/register.html', context)


class UserProfile(LoginRequiredMixin, UpdateView):
    form_class = UserProfileInfoForm
    template_name = "account/profile.html"
    queryset = UserProfileInfo.objects.all()
    context_object_name = 'profile'
    slug_field = 'id'
    login_url = 'login'
    success_url = '/'


"""
##########################################
##  Developed By:Mustafa Raad Mutashar  ##
##  mustafa.raad.7@gmail.com     2020   ##
##########################################
"""
