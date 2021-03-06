from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.http import HttpResponseRedirect
from django.urls  import reverse


def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else :
        post.likes.add(request.user)  
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self,**kwargs):
        data=super().get_context_data(**kwargs)
        likes_connected=get_object_or_404(Post,id=self.kwargs['pk'])
        liked=False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked=True
        data['number_of_likes']=likes_connected.number_of_likes()
        data['post_is_liked'] =liked
        return data   



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


