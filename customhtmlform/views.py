from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = ContactForm()
    return render(request, 'customhtmlform/contact.html', {'form': form})
