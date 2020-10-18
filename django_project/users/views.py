from django.shortcuts import render, redirect
#django itself provide a user registration creation form
from django.contrib.auth.forms import UserCreationForm

#IMPORTING MEASSAGES FROM DJANGO , THERE ARE SEVERAL MESSAGES LIKE messages.info, messages.success etc.
from django.contrib import messages 

# Create your views here.
#creating the visual look of users app and the we import this path to the main project
def register(request):
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username =  form.cleaned_data.get('username')
               messages.success(request, f'Account created for {username}!')
               #after submitting return to the home page
               return redirect('blog-home')
     else:
          form = UserCreationForm()
     return render(request, 'users/register.html', {'form':form})


