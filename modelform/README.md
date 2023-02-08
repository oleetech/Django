
![Logo](https://i.postimg.cc/4NTJn53b/djangomodelform.png)
# Django Model Form 

## Create App And Linking App myapp name 'modelform'

**djangoproject/settings.py**
```python
INSTALLED_APPS = [
    'modelform',
    'itemapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

**modelform/urls.py**
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_person, name='modelform'),
]
```
**modelform/views.py**
```python
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

```
**djangoproject/urls.py**
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modelform/',include('modelform.urls')),

]
```
**modelform/models.py**
```python
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
```
**modelform/forms.py**
```python
from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
```
**modelform/templates/modelform/person.html**
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
  </form>
```
## Screenshots

![App Screenshot](https://i.postimg.cc/V62xRRQF/simpleform.png)        





