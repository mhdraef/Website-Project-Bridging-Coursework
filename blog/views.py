from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(date_published__isnull=False).order_by('-date_published')
    return render(request, 'blog/post_list.html', {'posts':posts})

def blog_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_post.html', {'post': post})
