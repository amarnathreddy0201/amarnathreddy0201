from email import message_from_string
from email.errors import MessageParseError
from email.mime import base
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room, Topic,Message
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# rooms=[
#     {"id":1,"name":"Lets learn python"},
#     {"id":2,"name":"Design with me"},
#     {"id":3,"name":"Frontend Developer"}
#     ]
# Create your views here.

def login_page(request):
    page='login'
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method== 'POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"User doesn't exist")
            
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'user name or password not exist')
    context={"page":page}
    return render(request,'base/login_register.html',context)

def login_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    page='register'
    form= UserCreationForm()
    if request.method =="POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error occured Turnning Registration')

    return render(request,'base/login_register.html',{'form':form})
def home(request):
    q=request.GET.get('q') if request.GET.get('q') is not None else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__contains=q)|
        Q(description__icontains=q)
        
        )
    topics=Topic.objects.all()
    room_count=rooms.count()
    room_messages=Message.objects.filter(
        Q(room__topic__name__icontains=q)
    )

    context={'room_messages':room_messages,'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request,"base/home.html",context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all()#.order_by('-created')
    participants=room.participants.all()
    if request.method=="POST":
        message=Message.objects.create(user=request.User,
        room=room,
        body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)

    context={'room':room,'room_messages':room_messages,"participants":participants}
    return render(request,"base/room.html",context)

def user_profile(request,pk):
    user=User.objects.get(id=pk)
    rooms=user.room_set.all()
    room_messages=user.message_set.all()
    topics=Topic.objects.all()

    context={'topics':topics,'user':user,'room':rooms,'room_messagess':room_messages,}
    return render(request,'base/profile.html',context)


@login_required(login_url='/login')
def create_room(request):
    form=RoomForm()
    if request.method=="POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            room=form.save(commit=False)
            room.host=request.user
            room.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)

@login_required(login_url='/login')
def update_room(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)

    if request.user!= room.host:
        return HttpResponse('your are not allowed here !!')
    if request.method=="POST":
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context={'form':form}
    return render(request,'base/room_form.html',context)

def delete_room(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=="POST":
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})

@login_required(login_url='login')
def delete_message(request,pk):
    message=Message.objects.get(id=pk)
    if request.user !=  message.user:
        return HttpResponse( 'Your are not allowed here !!!')
    if request.method=="POST":
        message.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':message})
