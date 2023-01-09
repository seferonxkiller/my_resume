from django.shortcuts import render
from .models import *
from post.models import *
from person.models import *
from .forms import GitInTouchForm

# Create your views here.


def home(request):
    posts = Post.objects.order_by('-id')
    form = GitInTouchForm(request.POST or None)
    if form.is_valid():
        form.save()
    projects = Projects.objects.order_by('-id')
    services = Service.objects.order_by('-id')
    resumes = Resume.objects.all()
    abouts = About.objects.order_by('-id')
    partners = Partner.objects.all()
    s = request.GET.get('s')
    if s:
        posts = posts.filter(title__icontains=s)
    ctx = {
        'posts': posts[:3],
        'form': form,
        'projects': projects[:6],
        'services': services[:6],
        'resumes': resumes,
        'abouts': abouts[:1],
        'partners': partners
    }
    return render(request, 'index.html', ctx)
