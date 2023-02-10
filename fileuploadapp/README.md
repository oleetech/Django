
# File Upload App

## Create App 
```bash
python manage.py startapp fileuploadapp
```
## Link With Django Project

***djangoproject/settings.py***
```python
INSTALLED_APPS = [
    'fileuploadapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

****include urls.py |Djangoproject Folder ****
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fileupload/',include('fileuploadapp.urls')),

]
```

### Make Models
***models.py***
```python
from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    description = models.TextField(blank=True)
```

### Make Migrations And Migrate
```bash
python manage.py makemigrations
python manage.py Migrate
```


### forms.py
**create a forms.py file in fileuploadapp app folder**
```python
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'file', 'description']
```
***views.py***
```python
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'fileuploadapp/document_list.html', {'documents': documents})


def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'fileuploadapp/document_upload.html', {'form': form})


def document_update(request, pk):
    document = Document.objects.get(pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'fileuploadapp/document_update.html', {'form': form})


def document_delete(request, pk):
    Document.objects.get(pk=pk).delete()
    return redirect('document_list')

```

## templates file
***document_upload.html***
```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
  ```
***document_list.html***
```html
<h1>Document List</h1>
<a href="{% url 'document_create' %}">Create Document</a>
<table>
    <tr>
        <th>Title</th>
        <th>File</th>
        <th>Description</th>
        <th>Actions</th>
    </tr>
    {% for document in documents %}
    <tr>
        <td>{{ document.name }}</td>
        <td><a href="{{ document.file.url }}">{{ document.file.name }}</a></td>
        <td>{{ document.description }}</td>
        <td>
            <a href="{% url 'document_update' document.pk %}">Edit</a>
            <a href="{% url 'document_delete' document.pk %}" onclick="return confirm('Are you sure?')">Delete</a>
        </td>
    </tr>
    {% endfor %}
</table>
```
***document_update.html***
```html
<h1>Update Document</h1>
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Update</button>
</form>
```


***urls.py***
```python
from django.urls import path
from .views import document_list, document_create, document_update, document_delete

urlpatterns = [
    path('', document_list, name='document_list'),
    path('create/', document_create, name='document_create'),
    path('update/<int:pk>/', document_update, name='document_update'),
    path('delete/<int:pk>/', document_delete, name='document_delete'),
]
```
![App Screenshot](https://i.postimg.cc/05T1vgzG/createpage.png)

![App Screenshot](https://i.postimg.cc/RZ9r3cQN/listpage.png)


![App Screenshot](https://i.postimg.cc/3xZs2dn9/updatepage.png)

![App Screenshot](https://i.postimg.cc/7YS8YBzF/Delete-Page.png)
