from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # handle form processing here
            # ...
            return HttpResponse('Yes Form Is Valid')
    else:
        form = ContactForm()

    return render(request, 'formapp/contact.html', {'form': form})

# Create your views here.
