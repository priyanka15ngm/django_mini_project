from django.shortcuts import render
#importing post from models so we can access post and content that we created in the sql database after migratons using commands and after that we can edit that data using admin panel
from .models import Post

'''posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'

    },

    {
        'author': 'PriyankaER',
        'title': 'Blog Post',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'


    }


]'''



def home(request):
    context = {
        'posts' : #posts 
                    #this is a dummy data of list posts
                  Post.objects.all()
                    #this returns the data that we created in database
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})


