from django.shortcuts import render,redirect
import datetime as datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image,Profile,Comments
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,ProfileForm

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

@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    image = Image.objects.filter(user=current_user)
    profile = Profile.objects.filter(user=current_user).first()
    return render(request,'nu_profile.html',{"image":image,"profile":profile})

@login_required(login_url='/accounts/login')    
def nu_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')  
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form":form}) 

@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    image = Image.objects.filter(user=current_user).all()
    profile = Profile.objects.filter(user=current_user).first()
    return render(request,'nu_profile.html',{"image":image,"profile":profile})
 
@login_required(login_url='/accounts/login/')
def search(request):
   if 'username' in request.GET and request.GET["username"]:
       search_term = request.GET.get("username")
       searched_users = Profile.search_by_profile(search_term)
       print(searched_users)
       message = f"{search_term}"
       return render(request, "search.html",{"message":message,"users": searched_users})
   else:
       message = "You haven't searched for any term"
       return render(request, 'search.html',{"message":message})
            
            
                
