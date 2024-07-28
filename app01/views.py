from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

app_name='tasks'
def index(request):
    return render(request, 'app01/index.html')