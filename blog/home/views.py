from django.shortcuts import render
from home.models import Blog,Contact
import math

def home(request):
    return render(request,'home.html')

def blog(request):
    no_of_posts=4
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page=int(page)
    if page>1:
        prev=page-1
    else:
        prev=None
    blogs=Blog.objects.all()
    l=len(blogs)
    if page<math.ceil(l/no_of_posts):
        nxt=page+1
    else:
        nxt=None
    blogs=Blog.objects.all()[(page-1)*no_of_posts:page*no_of_posts]
    context={'blogs':blogs,'prev':prev,'nxt':nxt}
    return render(request,'blog.html',context)

def blogpost(request, slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render(request,'blogpost.html',context)

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        ins=Contact(name=name,phone=phone,email=email,desc=desc)
        ins.save()
    return render(request,'contact.html')

def search(request):
    return render(request, 'search.html')