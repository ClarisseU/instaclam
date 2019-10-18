from django.shortcuts import render,redirect
import datetime as datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image,Profile,Comments
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm

@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'welcome.html', {'images':images})

@login_required(login_url='/accounts/login')
def post(request,id):
    try:
        images = Image.objects.get(id=id)
    except DoesNotExist:
        raise Http404
    return render(request, 'welcome.html',{'image':images})

@login_required(login_url='/accounts/login')
def new_post(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('welcome')
    
    else:
        form = NewPostForm()
    return render (request, 'new_post.html', {"form":form})        
