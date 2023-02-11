
![Logo](https://blueshelltech.com/media/2021/05/python-django.png)
# Table Of Content

  * [Setup Virtual Environment](#setup-virtual-environment)
  * [Installation virtualenv](#installation-virtualenv)
  * [Create A Folder For Virtual Environment](#create-a-folder-for-virtual-environment)
- [Create Django Project](#create-django-project)
  * [Create A Django App](#create-a-django-app)
    + [Linking Blog App With Django Project](#linking-blog-app-with-django-project)
    + [Run Server](#run-server)
## Setup Virtual Environment


## Installation virtualenv 

Install virtualenv by running the command
```bash
pip install virtualenvt
```
    
## Create A Folder For Virtual Environment 
1.Create A Folder For Create Virtual Environment Example myfolder

2.open 'myfolder' directory in command prump

```bash
virtualenv venv
```

3 . Navigate script directory 

```bash 
 cd myfolder\venv\Scripts
 ```

 4. Activate virtual invirnement by type
 ```bash
 activate
 ```

 5. Install Django in the virtual environment by running the command 
 ```bash
 pip install django
 ```
6. Create a new Django project by running the command
```bash
django-admin startproject projectname
```
7. Run the server by running the command 
```bash
python manage.py runserve
```
8. To exit the virtual environment, run the command
```bash
deactivate
```
 

# Create Django Project
 inside virtual env folder run the command . this will Create A folder name DjangoProject.
 Start a new Django project:
 ```bash
 django-admin startproject Djangoproject
```
## Create A Django App
inside Djangoproject Folder Run Code In CMD
```bash
python manage.py startapp blog
```
### Linking Blog App With Django Project
open Djangoproject settings.py

```python
# Application definition

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

create a **urls.py** inside blog app . after open Djangoproject **urls.py** . Link app urls.py with Djangoproject urls.py

**Djangoproject/urls.py**
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls'))
]
```
**blog/urls.py**
```python
from django.urls import path

from . import views
urlpatterns=[
    
]
```
### Run Server
inside Djangoproject Folder The Command In Cmd
```bash
python manage.py runserver
```













