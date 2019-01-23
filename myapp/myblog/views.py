from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView

from myblog.models import Post


class PostListView(ListView):
    template_name = "post_list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class PostCreateView(CreateView):
    template_name = "post_create.html"
    model = Post
    fields = ['author', 'title', 'text']
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    template_name = "post_update.html"
    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy('post_list')
