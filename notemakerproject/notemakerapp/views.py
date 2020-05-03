from django.shortcuts import render
from django.contrib.auth.models import User
from notemakerapp.models import Note
from notemakerapp.forms import UserForm,NoteForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'notemakerapp/index.html')

def about(request):
    return render(request,'notemakerapp/about.html')

@login_required
def special(request):
    return HttpResponse('You are logged in!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register_view(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(user_form.errors)

    else:
        user_form=UserForm()

    return render(request,'notemakerapp/register.html',{'user_form':user_form,
                                                        'registered':registered})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
               print('Account not active')
        else:
            print('Username{}and password{}'.format(username,password))
    else:
        return render(request,'notemakerapp/login.html',{})

def note_add_view(request):
    if request.method=="POST":
        note_form=NoteForm(data=request.POST)
        if note_form.is_valid():
            note_form.save()
        else:
            print('Error in validation')
    else:
        note_form=NoteForm()
    return render(request,'notemakerapp/note_form.html',{'note_form':note_form})


def notes_view(request):
    logged_in_user = request.user
    logged_in_user_posts = Note.objects.filter(user=logged_in_user)
    return render(request, 'notemakerapp/notes.html', {'notes': logged_in_user_posts})
