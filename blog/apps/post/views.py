from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-created_at')