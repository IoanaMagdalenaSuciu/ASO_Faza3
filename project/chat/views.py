from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from account.views import login_view
from chat.models import Chat, Message

User = get_user_model()


def home(request):

    if request.user.is_authenticated:
        user = request.user
        chats = request.user.chat_set.all()
        return render(request, "mainpage.html", {'chats': chats})
    else:
        return redirect(login_view)

@login_required
def chat(request, chat):

    username = request.GET.get('username')
    chat_details = Chat.objects.get(name=chat)
    chat_users = chat_details.users.all()
    all_users = User.objects.filter()
    return render(request, 'privateChat.html', {
        'username': username,
        'chat': chat,
        'chat_details': chat_details,
        'all_users': all_users,
        'chat_users': chat_users
    })

@login_required
def private_chat(request):
    chat = request.POST['chat_name']
    user = request.user

    if Chat.objects.filter(name=chat).exists():
        return redirect('/' + chat + '/?username=' + user.username)
    else:
        new_chat = Chat.objects.create(name=chat)
        new_chat.save()
        new_chat.users.add(user)
        return redirect('/'+chat+'/?username='+user.username)

@login_required
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    chat_name = request.POST['chat_name']

    new_message = Message.objects.create(sender=username, chat=chat_name, text=message)
    print(new_message)
    new_message.save()
    return HttpResponse('Message sent successfully')

@login_required
def getMessages(request, chat):
    chat = Chat.objects.get(name=chat)

    messages = Message.objects.filter(chat=chat.name)
    return JsonResponse({"messages":list(messages.values())})

@login_required
def invite(request):
    new_user = request.POST['new_user']
    chat_name = request.POST['chat_name']
    user = User.objects.filter(username=new_user)[0]
    chat = Chat.objects.filter(name=chat_name)[0]
    chat.users.add(user.id)
    return HttpResponse('User added')
