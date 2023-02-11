# Django Image Upload Crud
```bash
  ____      _                                     ___                                        _   _           _                       _ 
 |  _ \    (_)   __ _   _ __     __ _    ___     |_ _|  _ __ ___     __ _    __ _    ___    | | | |  _ __   | |   ___     __ _    __| |
 | | | |   | |  / _` | | '_ \   / _` |  / _ \     | |  | '_ ` _ \   / _` |  / _` |  / _ \   | | | | | '_ \  | |  / _ \   / _` |  / _` |
 | |_| |   | | | (_| | | | | | | (_| | | (_) |    | |  | | | | | | | (_| | | (_| | |  __/   | |_| | | |_) | | | | (_) | | (_| | | (_| |
 |____/   _/ |  \__,_| |_| |_|  \__, |  \___/    |___| |_| |_| |_|  \__,_|  \__, |  \___|    \___/  | .__/  |_|  \___/   \__,_|  \__,_|
         |__/                   |___/                                       |___/                   |_|                                
```
A brief description of the project and its purpose.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Base Template](#base-template)  
   - [Create App](#create-app)
   - [App Link With Project](#app-link)
     - [settings.py](#settings)
     - [app urls.py](#urls.py)
     - [views.py](#views.py)
     - [project urls.py](#project-urls.py)

   - [Create Model](#create-model)
   - [Run migrations:](#run-migration)
   - [Create Form :](#form)
   - [Create Route :](#route)
   - [Create View :](#views)
   - [Create Template :](#template)
3. [Screen Shot](#screen-shot)

4. [Authors](#suthors)
5. [Demo](#demo)


## Introduction :
Django is a high-level web framework that allows developers to create powerful and dynamic web applications quickly and efficiently. One of the common features of web applications is the ability to manage images, and in this tutorial, we will show you how to create a simple image CRUD (Create, Read, Update, Delete) system using Django. This tutorial is aimed at beginner Django developers who want to learn how to create a simple image management system in Django. We will cover the basics of Django models, views, and templates, and how to use them to create a functional image CRUD system. By the end of this tutorial, you will have a basic understanding of how to create, read, update, and delete images in Django.
## Getting Started :
Pillow is a library in Python that allows you to work with images. In this image CRUD system, we will be using Pillow to handle and manipulate image files. Installing Pillow is a crucial step in setting up our project because without it, we will not be able to process the images in our application.

To install Pillow, simply run the following command in your terminal or command prompt:

```bash
pip install Pillow
```
This will install the latest version of Pillow on your system and make it available for use in your Django project. With Pillow installed, we will be able to handle image files, resize images, and perform other .



### Installation :
To create a new Django project, you will need to open your terminal or command prompt and run the following command:

```bash
django-admin startproject djangoproject
```
### Base Template :
First, create a new templates directory in the project directory (not the app Folder):

add the template directory to the TEMPLATES option in the settings.py file of the project

```python
'DIRS': [BASE_DIR / 'templates' ],

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```
create base.html in the templates
```html
{%load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{% if title %} {{title}} {% else %} Post  {% endif %}</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
            <link rel="stylesheet" href="{% static 'css/style.css' %}" />

    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
</html>
```
create a folder name static inside project directory

create three directories js, css, and images directory inside the static directory:


```bash
├── static
|  ├── css
|  ├── images
|  └── js
```
### Create App :
Next, navigate into the project directory using the following command:
```bash
python manage.py startapp imagecrud
```
### App Link With Project :
To link your app to your project, you need to add it to the INSTALLED_APPS list in the settings.py file of your project.
#### settings.py :
Open the settings.py file in your project directory and add the following line to the INSTALLED_APPS list:
```python
INSTALLED_APPS = ['imagecrud',]
```
For Working With Image Need This 
```python
# Base url to serve media files  
MEDIA_URL = '/media/'  
  
# Path where media is stored  
MEDIA_ROOT = [BASE_DIR / 'media/']  
```
MEDIA_URL - It will serve the media files.
MEDIA_ROOT - It specifies the path of the root where file will be stored.

#### urls.py :
To create a URL pattern for your app, you need to create a urls.py file inside your app directory and define your URL patterns there.

Here's an example of what your urls.py file might look like:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```
#### views.py:
For Work home link properly views.py file might look like:
```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('success')
```  

#### Django project urls.py
```python
from django.urls import path,include
from django.conf import settings  
from django.conf.urls.static import static  
urlpatterns = [
    path('imagecrud/',include('imagecrud.urls')),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
```
### Create Model :
```python
from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name)  
```
### Run migrations :
```bash
 python manage.py makemigrations
 python manage.py migrate
```
### Create Form :
```python
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image']
```        
### Create Route :
```python

from django.urls import path
from .views import index, add_image, update_image, delete_image

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_image, name='add_image'),
    path('update/<int:pk>/', update_image, name='update_image'),
    path('delete/<int:pk>/', delete_image, name='delete_image'),
]

```
### Create View :
```python
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def index(request):
    images = Image.objects.all()
    return render(request, 'image_upload/index.html', {'images': images})

def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageForm()
    return render(request, 'image_upload/add_image.html', {'form': form})

def update_image(request, pk):
    image = Image.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageForm(instance=image)
    return render(request, 'image_upload/update_image.html', {'form': form})

def delete_image(request, pk):
    Image.objects.filter(pk=pk).delete()
    return redirect('index')
```    
### Create Template :
Create a template for the image upload form in the templates directory:

templates/imagecrud/index.html
```html
<h1>Image Uploads</h1>
<a href="{% url 'add_image' %}">Add Image</a>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Image</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {% for image in images %}
    <tr>
      <td>{{ image.name }}</td>
      <td><img src="{{ image.image.url }}" width="100" height="100"></td>
      <td>
        <a href="{% url 'update_image' image.pk %}">Edit</a>
        <a href="{% url 'delete_image' image.pk %}" onclick="return confirm('Are you sure?')">Delete</a>
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
```

templates/imagecrud/add_image.html:
```html
<h1>Add Image</h1>
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
```
templates/imagecrud/update_image.html:
```html
<h1>Edit Image</h1>
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
```
## Screen Shot
![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Authors

- [@oleetech](https://www.github.com/oleetech)

## Demo

Insert gif or link to demo
