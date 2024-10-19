from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Room, Message,UserQueries
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .models import Background
from .forms import LoginForm, SignUPForm
def home(request):
    return render(request, 'home.html')
from .models import Room
@login_required
def infra(request):
    return render(request, 'infra.html')
@login_required
def edu(request):
    return render(request, 'edu.html')
@login_required
def security(request):
    if request.method == 'POST':
        mess = request.POST['txt']
        usr = request.user
        try:
          Message.objects.create(message=mess, username=usr)
          message = Message.objects.all()
          return render(request, 'security.html', {"messages":message})
        except:
           return HttpResponse('ERROR')
    else:
        return render(request, 'security.html')

        

    
    
@login_required
def health(request):
    API_KEY = 'dfa5d1a88fdc4465aca2a49e58f116bb'
    country = 'us'
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category=health&apiKey={API_KEY}'
    response = requests.get(url)
    json_data = response.json()
    articles = json_data['articles']
    context =  {"articles":articles}
    return render(request, 'health.html', context)
@login_required
def enter(request):
    API_KEY = 'dfa5d1a88fdc4465aca2a49e58f116bb'
    country = 'us'
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category=entertainment&apiKey={API_KEY}'
    response = requests.get(url)
    json_data = response.json()
    articles = json_data['articles']
    context =  {"articles":articles}
    return render(request, 'health.html', context)
    return render(request, 'enter.html')
def usersignup(request):
    if request.method == "POST":
        form = SignUPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUPForm()

    return render(request, "signup.html", {"form": form})



def userlogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("enter")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def engage(request):

    return render(request, 'engage.html')

def aboutus(request):
    return render(request, 'aboutus.html')



@csrf_exempt
def chat_view(request):
    user = request.user  

    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        
       
        UserQueries.objects.create(sender='user', user=user, message=user_message)

        return JsonResponse({'status': 'Message sent!'})

    
    messages = UserQueries.objects.filter(user=user).order_by('timestamp')
    messages_data = [{'sender': msg.sender, 'message': msg.message} for msg in messages]
    return JsonResponse({'messages': messages_data})