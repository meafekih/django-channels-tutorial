from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Message
from django.contrib.auth.models import User
from channels.db import database_sync_to_async


def index(request):
    return render(request, "index.html", {})

def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})

@database_sync_to_async
def get_user(username):
    return User.objects.get(username=username)[0]



