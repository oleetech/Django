from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonForm


def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = PersonForm()
    return render(request, 'modelform/person.html', {'form': form})

