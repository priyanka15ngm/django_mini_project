# from django.shortcuts import render, redirect
from django.shortcuts import render, redirect

#django itself provide a user registration creation form
#replacing UserCreationForm with UserRegisterForm

#from django.contrib.auth.forms import UserCreationForm

#IMPORTING MEASSAGES FROM DJANGO , THERE ARE SEVERAL MESSAGES LIKE messages.info, messages.success etc.
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



#IMPORTING FORMS FROM forms.py



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

     if request.method == 'POST':

          u_form =  UserUpdateForm(request.POST, instance = request.user) 
          p_form = ProfileUpdateForm( request.POST,
                                      request.FILES,
                                      instance = request.user.profile)

          if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

     else:
          u_form = UserUpdateForm(instance=request.user)
          p_form = ProfileUpdateForm(instance=request.user.profile)

     
     context = {
          'u_form' : u_form,
          'p_form' : p_form
     } 
     return render(request, 'users/profile.html', context)


