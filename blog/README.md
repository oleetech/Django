```bash
                   _          _               _             ____                           _   
                  / \      __| |  _ __ ___   (_)  _ __     |  _ \    __ _   _ __     ___  | |  
                 / _ \    / _` | | '_ ` _ \  | | | '_ \    | |_) |  / _` | | '_ \   / _ \ | |  
                / ___ \  | (_| | | | | | | | | | | | | |   |  __/  | (_| | | | | | |  __/ | |  
               /_/   \_\  \__,_| |_| |_| |_| |_| |_| |_|   |_|      \__,_| |_| |_|  \___| |_|  
                       ____                      _ 
                      / ___|  _ __   _   _    __| |
                     | |     | '__| | | | |  / _` |
                     | |___  | |    | |_| | | (_| |
                      \____| |_|     \__,_|  \__,_|
                                                   
``` 
# Django Admin Panel Crud
```bash
python manage.py startapp blog
```

## Create App And Linking App myapp name 'customhtmlform'

**djangoproject/settings.py**
```python
INSTALLED_APPS = [
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

**blog/urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
]
```
**blog/views.py**

**blog/models.py**
```python
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.

```


## Make Migration
```bash
python manage.py makemigrations
```
## Migrate
```bash
python manage.py migrate
```
### Creating a superuser account
```bash
python manage.py createsuperuser
```

It’ll prompt for a username, email address, and password:

```bash
Username: olee          
Email address: olee.techs@gmail.com
Password: 
Password (again): 
Superuser created successfully.
```
### Start Server
```bash
python manage.py runserver
```
## Login Admin panel

![App Screenshot](https://www.pythontutorial.net/wp-content/uploads/2022/11/django-admin-page-admin-panel.png) 

## Add Model To Admin Panel Area
**blog/admin.py**
```python
from django.contrib import admin
from .models import Post


admin.site.register(Post)
```


![App Screenshot](https://www.pythontutorial.net/wp-content/uploads/2022/11/django-admin-page-blog.png)  

![App Screenshot](https://www.pythontutorial.net/wp-content/uploads/2022/11/django-admin-page-create-a-post.png)  


## Display data from the database

**blog/urls.py**
```python
from django.urls import path

from . import views
urlpatterns=[
    path('', views.blog, name='blog'),
    path('home/',views.home,name='home'),
]
```


**blog/views.py**
```python
from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


```

blog/templates/blog/home.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>My Posts</h1>
	{% for post in posts %}
		<h2>{{ post.title }}</h2>
		<small>Published on {{ post.published_at | date:"M d, Y" }} by {{ post.author | title}}</small>
		<p>{{ post.content }}</p>
	{% endfor %}
</body>
</html>
```

# Tinymce Editor Integration 
![App Screenshot](https://www.section.io/engineering-education/integrating-django-with-tinymce/tinymce-the-final-results.jpg)  



## Installation 
```bash
pip install django-tinymce
```
## Link With Django Project

```python
   INSTALLED_APPS = [
     #...
    'myapp',
    'tinymce',
    ]
```
## Setup Tinymce With Model
```python
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
## Add This Line
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = HTMLField() # Change This Line
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

### Refresh The Browser 
## Change Html Tempalte Tag
```html
<body>
    <h1>My Posts</h1>
	{% for post in posts %}
		<h2>{{ post.title }}</h2>
		<small>Published on {{ post.published_at | date:"M d, Y" }} by {{ post.author | title}}</small>

		<p>{{ post.content|safe }}</p> <!-- Change This Line -->
	{% endfor %}
</body>
```


## Screenshots

    





