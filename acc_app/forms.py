from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from acc_app.models import UserProfileInfo


class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('college', 'profile_pic',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["college"].label = "College"
        self.fields["profile_pic"].label = "Personal photo"


"""
##########################################
##  Developed By:Mustafa Raad Mutashar  ##
##  mustafa.raad.7@gmail.com     2020   ##
##########################################
"""
