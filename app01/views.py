from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

todos = ['foo', 'bar', 'baz']

app_name='tasks'
def index(request):
    return render(request, 'app01/index.html', {
        'todos': todos
    })


def add(request):
    return render(request, 'app01/add.html')