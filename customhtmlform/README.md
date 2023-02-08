```bash
 ____      _                                     _____                                 ____                 _                           _   _   _                 _ 
 |  _ \    (_)   __ _   _ __     __ _    ___     |  ___|   ___    _ __   _ __ ___      / ___|  _   _   ___  | |_    ___    _ __ ___     | | | | | |_   _ __ ___   | |
 | | | |   | |  / _` | | '_ \   / _` |  / _ \    | |_     / _ \  | '__| | '_ ` _ \    | |     | | | | / __| | __|  / _ \  | '_ ` _ \    | |_| | | __| | '_ ` _ \  | |
 | |_| |   | | | (_| | | | | | | (_| | | (_) |   |  _|   | (_) | | |    | | | | | |   | |___  | |_| | \__ \ | |_  | (_) | | | | | | |   |  _  | | |_  | | | | | | | |
 |____/   _/ |  \__,_| |_| |_|  \__, |  \___/    |_|      \___/  |_|    |_| |_| |_|    \____|  \__,_| |___/  \__|  \___/  |_| |_| |_|   |_| |_|  \__| |_| |_| |_| |_|
         |__/                   |___/                                  



  / _ \  | |   ___    ___  |_   _|   ___    ___  | |__  
 | | | | | |  / _ \  / _ \   | |    / _ \  / __| | '_ \ 
 | |_| | | | |  __/ |  __/   | |   |  __/ | (__  | | | |
  \___/  |_|  \___|  \___|   |_|    \___|  \___| |_| |_|
                                                        

``` 
# Django Model Customize html  Form 

## Create App And Linking App myapp name 'customhtmlform'

**djangoproject/settings.py**
```python
INSTALLED_APPS = [
    'customhtmlform',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

**customhtmlform/urls.py**
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='customhtmlform'),
]
```
**customhtmlform/models.py**
```python
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
```

**customhtmlform/forms.py**
```python
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-class'}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
```


**customhtmlform/views.py**
```python
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

```


**djangoproject/urls.py**
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [

    path('customhtlform/',include('customhtmlform.urls')),

]

```


**modelform/templates/modelform/person.html**
```html
<form method="post">
    {% csrf_token %}
    <div>
      <label for="{{ form.name.id_for_label }}">Name:</label>
      {{ form.name }}
    </div>
    <div>
      <label for="{{ form.email.id_for_label }}">Email:</label>
      {{ form.email }}
    </div>
    <div>
      <label for="{{ form.message.id_for_label }}">Message:</label>
      {{ form.message }}
    </div>
    <button type="submit">Submit</button>
  </form>


```
## Screenshots

![App Screenshot](https://i.postimg.cc/V62xRRQF/simpleform.png)        





