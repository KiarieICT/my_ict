from django.shortcuts import render,redirect
from .forms import lets_connect


# Create your views here.
def profile(request):
    return render(request,"home/profile.html",{'form':lets_connect})
