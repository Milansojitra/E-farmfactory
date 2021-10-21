from django.shortcuts import render,get_object_or_404,redirect
from .models import post
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q


class postListView(ListView):
    model = post
    template_name = "farmtube/postlist.html"
    ordering=['-date_posted']
    context_object_name='posts'
    paginate_by = 4
    


class postDetailView(DetailView):
    model = post
    context_object_name='post'
    template_name = "farmtube/postdetail.html"


class postCreateView(LoginRequiredMixin,CreateView):
    model = post
    fields=['title','content','tags','Video']
    template_name = "farmtube/postcreate.html"
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class searchView(ListView):
    model = post
    template_name = "farmtube/postlist.html"
    context_object_name='posts'
    paginate_by = 4
    ordering=['-date_posted']

    def get_queryset(self):
        query=self.kwargs.get('query')
        return post.objects.filter(Q(title__icontains=query)|Q(content__icontains=query)|Q(tags__slug__icontains=query)).distinct()



class authorListView(ListView):
    model = post
    template_name = "farmtube/postlist.html"
    ordering=['-date_posted']
    context_object_name='posts'
    paginate_by = 5
    
    def get_queryset(self):
        author=get_object_or_404(User,username=self.kwargs.get('username'))
        return post.objects.filter(author=author)

class postUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=post
    fields=['title','content','Video','tags']
    template_name='farmtube/postcreate.html'
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    
    
class postDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post
    template_name='farmtube/delete.html'
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


class taggitListView(ListView):
    model = post
    template_name = "farmtube/postlist.html"
    ordering=['-date_posted']
    context_object_name='posts'
    paginate_by = 5
    
    def get_queryset(self):
        return post.objects.filter(tags__slug=self.kwargs.get('slug'))