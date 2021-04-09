import json
from functools import lru_cache
from django.shortcuts import render, Http404
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from .models import Chat


@login_required(login_url='/login')
@lru_cache
def room(request, room_name):
    username = request.user.username
    chat = Chat.objects.filter(roomname=room_name)
    if chat.exists():
        if room_name == username or request.user.is_superuser:
            # for member in chat.members:
            # if user == chat.members.:
            context = {
                'room_name': room_name,
                'username': mark_safe(json.dumps(username))
            }
            return render(request, "chat/room.html", context)
    raise Http404()
