
# Create A App
```bash
python manage.py startapp formapp
```

## Link With Django Project 
**djangoproject/settings.py**
```python
INSTALLED_APPS = [
    'formapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Linking App urls.py To Project urls.py 
**formapp/views.py**
```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
 return HttpResponse('hello')

```

**formapp/urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home')
]
```



**djangoproject/urls.py**
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formapp/',include('formapp.urls'))

]
```
# Create Simple Form

1. Create a forms.py file in your app directory and define the form

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea)

```


2. create file contact.html inside formapp/templates/formapp/contact.html . 

3. Create a view to handle the form submission:

```python
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


```
4. templates/formapp/create.html content like Below
```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="Submit">
</form>
```
5. formapp/urls.py like Below
```python
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
]
```




## Screenshots

![App Screenshot](https://i.postimg.cc/V62xRRQF/simpleform.png)

