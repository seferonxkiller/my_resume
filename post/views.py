from django.shortcuts import render
from .models import *
from .forms import CommentForm

# Create your views here.


def blog_single(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        commit = form.save(commit=False)
        commit.post = post
        commit.save()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    ls = Post.objects.order_by('-id')
    ctx = {
        'form': form,
        'post': post,
        'tags': tags,
        'categories': categories,
        'last_3_posts': ls
    }
    return render(request, 'single.html', ctx)

