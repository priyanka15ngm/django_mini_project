from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
# importing post from models so we can access post and content that we created in the sql database after migratons using commands and after that we can edit that data using admin panel
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
        'posts':  # posts
        # this is a dummy data of list posts
        Post.objects.all()
        # this returns the data that we created in database
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
