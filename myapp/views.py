from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from  django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features} )

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):
    if  request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['repeat-password']
        
        if password == password2:
            if User.object.filter(email=email).exists():
                messages.info(request, 'Email has already been used')
            
        
        
        
    return render(request, 'register.html')