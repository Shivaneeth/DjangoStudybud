from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Python'},
    {'id': 2, 'name': 'Css'},
    {'id': 3, 'name': 'Html'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request):
    return render(request, 'room.html')
