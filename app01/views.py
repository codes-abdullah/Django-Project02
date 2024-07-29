from django.http import HttpResponse
from django.shortcuts import render
from django import forms

todos = ['foo', 'bar', 'baz']

class NewTaskForm(forms.Form):
    the_charfield = forms.CharField(label='my field')



todos = ['foo', 'bar', 'baz']
app_name='tasks'
def index(request):
    return render(request, 'app01/index.html', {
        'todos': todos
    })


def add(request):
    if request.method == "POST":
        f = NewTaskForm(request.POST)
        if f.is_valid():
            value = f.cleaned_data['the_charfield']
            todos.append(value)
            return render(request, 'app01/add.html', {
                'form': NewTaskForm(),
                'status': value+' - added successfully'
            })
        else:
            return render(request, 'app01/add.html', {
                'form':f
            })

    return render(request, 'app01/add.html', {
        'form': NewTaskForm()
    });
