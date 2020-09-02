# Create your views here.
from django.shortcuts import render,HttpResponseRedirect
from .models import *


# Create your views here.
def home(request):
    Post=post.objects.all()
    context={
'Post':Post

    }
    return render(request,'home.html',context)
def blogs(request,id,slug):
    Post=post.objects.filter(slug=slug).first()
    com=comments.objects.filter(id=id)
    context={
   'Post':Post,
   'com':com,

    }
    # if request.method == 'POST':
    #    name=request.POST['name']
    #    comment=request.POST['comment']
    #    con=comments(name=name,comment=comment)
    #    con.save()
    # else:
    #     con.comments()   
    return render(request,'post.html',context)
def search(request):

    query=request.GET['query']
    Post=post.objects.filter(name__icontains=query)    
    context={'Post':Post,
  
    }
    return render(request, 'home.html',context)