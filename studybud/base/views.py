from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Topic
from .forms import CreateRoomForm
from django.db.models import Q

def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    content = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', content)


def room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    content = {'room': room}
    return render(request, 'base/room.html', content)


def create_room(request):

    if request.method == "POST":
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')
        context = {'form': form}
        return render(request, 'base/create_form.html', context)

    else:
        form = CreateRoomForm()

        return render(request, "base/create_form.html", {"form": form})

# href="{% url'base:update' room.id %}
# href="/update/{{room.id}}


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = CreateRoomForm(instance=room)
    if request.method == "POST":
        form = CreateRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('base:room', pk)
        return redirect('base:update-room', pk)

    else:
        form = CreateRoomForm(instance=room)
        context = {'form': form}
        CreateRoomForm(instance=room)
        return render(request, "base/update_form.html", context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    return render(request, 'base/delete_room.html', {'obj':room})
