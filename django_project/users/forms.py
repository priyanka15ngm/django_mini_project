#importing forms
from django import forms
#importing models
from django.contrib.auth.models import User
#importing UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

#in meta we use a model of User form
# this class meta gives us nested namespace for configurations and keeps the configurations in one place and within the configuration we're saying that the model will be affected is the
# so for example when we do a form.save() it;s going to save it to this user model and the fields taht we have there in the list are the fields that we want in the form and in what order okay so this is now our completed form that inherits from the user creation form and adds this email field and now we can just use this
#this form in our view instead of the user creation and then taht should make it good to go so let's go back to our views here and at the top let's inherit the form that we just created.



    class Meta:
        model = User
        #in fields we write those field that gonna shown up on form
        fields = ['username', 'email', 'password1', 'password2']

#this ia a user update form
class UserUpdateForm(forms.ModelForm):
    email =  forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
#this is a profile update form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model =  Profile
        fields = ['image']

