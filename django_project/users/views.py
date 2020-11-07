# from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#django itself provide a user registration creation form
#replacing UserCreationForm with UserRegisterForm

#from django.contrib.auth.forms import UserCreationForm

#IMPORTING MEASSAGES FROM DJANGO , THERE ARE SEVERAL MESSAGES LIKE messages.info, messages.success etc.
from django.contrib import messages 

#IMPORTING FORMS FROM forms.py

from .forms import UserRegisterForm

# Create your views here.
#creating the visual look of users app and the we import this path to the main project
def register(request):
     if request.method == 'POST':
          #form = UserCreationForm(request.POST)
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()
               username =  form.cleaned_data.get('username')
               messages.success(request, f'Your account has been created! You are now able to login')
               #after submitting return to the home page
               # return redirect('blog-home')
               return redirect('login')
     else:
          #form = UserCreationForm()
          form = UserRegisterForm()
     return render(request, 'users/register.html', {'form':form})

#this is call genova decorator which add extra functinality to profile that the user must be logged in to view this page(profile page)
@login_required
def profile(request):
     return render(request, 'users/profile.html')

