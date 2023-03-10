
# Django Login/Registraion


## Create A App name user

```bash
django-admin startapp users
```

***register the users application in the installed apps of the settings.py***

```python
INSTALLED_APPS = [
    'users',   
]
```

***urls.py | users app folder***
```python
from django.urls import path
from . import views

urlpatterns = []
```
Include  app urls.py to project urls.py

****urls.py | Djangoproject Folder****

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
]
```

## Create a login form
***urls.py | users Folder***

```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    ]
```
****forms.py | users App folder****
```python
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

```
***views.py | users app Folder***
```python
from django.shortcuts import render
from .forms import LoginForm


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

```
 *create the templates/users directory inside the users application:*
 
 ****templates/users/login.html| users app Folder****
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
    <form method="POST" novalidate>
        {% csrf_token %}
        <h2>Login</h2>
        {{form.as_p}}
        <input type="submit" value="Login" />
    </form>
    
</body>
</html>

```
## Form Output
![App Screenshot](https://i.postimg.cc/TP0Y21VZ/login.png)

## Form Processing  After submit

***views.py| users app Folder***

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import LoginForm


def sign_in(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('blog')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})
```


## Logout form
***urls.py |users app Folder***
```python
from django.urls import path
from . import views

urlpatterns = [
        path('login/', views.sign_in, name='login'),
        path('logout/',views.sign_out,name='logout'),

]
```

```python
from django.contrib.auth import login, authenticate, logout

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')  
 ```
## Log In User redirect
```python
        if request.user.is_authenticated:
            return redirect('posts')
 ``` 

 ## Login/Logout Link
 ```python
   		{%if request.user.is_authenticated %}
  			<span>Hi {{ request.user.username | title }}</span>
  			<a href="{% url 'logout' %}">Logout</a>
  		{%else%}
  			<a href="{% url 'login' %}">Login</a>
  		{%endif%}
```
![App Screenshot](https://i.postimg.cc/gJVrxmvF/loginlink.png)

![App Screenshot](https://i.postimg.cc/CKyq5vW8/logoutlink.png)

## Only Logged User Can Access
### Frontend Page Protect 
html template some section only for login user can view. suppose edit button and delete button only for registered user.
```html
		{% if request.user.is_authenticated %}
		<p>
			<a href="{% url 'post-edit' post.id %}">Edit</a> 
			<a href="{% url 'post-delete' post.id%}">Delete</a>
		</p>
		{% endif %}
```
### Backend Protect
**create, update, and delete post functions using the login_required decorator**
*****views.py*****
```python
from django.contrib.auth.decorators import login_required

@login_required
def delete_post(request, id):
  pass
  
@login_required
def edit_post(request, id):
  pass
  
@login_required
def create_post(request):
 pass
```
???????????? ????????? ??????????????? ????????????????????? ????????? ???????????? ??? ??????????????? ???????????? ?????????????????? ????????? ??????????????? ?????????????????? ???????????? accounts/login/ ?????? ??????????????? ?????????????????? ???????????? ???????????? ???????????? ???????????????  ?????????????????? ?????????????????? ???????????? ?????????????????? ????????? ???????????? users app ??? users/login/ ???????????????????????? ?????? ???????????? ???????????????????????? ???????????? ???????????????????????? ?????? settings.py ??????????????? login url ?????????????????? ????????? ????????? 

***settings.py|project Folder***

```python
LOGIN_URL = 'login'
```
# Registration Form

***urls.py | users app Folder***

```python
    path('register/', views.sign_up, name='register'),
```
***forms.py | users app Folder***

```python
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
```
***views.py | users app folder***

```python
from .forms import LoginForm,RegisterForm
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', { 'form': form})  
```
***Create a file Template/users/register.html Folder inside app folder***

```html
<form method="POST" novalidate>
	{% csrf_token %}
	<h2>Sign Up</h2>
	{{ form.as_p }}		
	<input type="submit" value="Register" />
</form>
```

*****Form Like This*****

![App Screenshot](https://i.postimg.cc/8ccjR8Ff/register.png)

******Customize the Django register form******

***templates/users/register.html***

```html
<form method="POST" novalidate>
	{% csrf_token %}
	<h2>Sign Up</h2>
		
	{% for field in form %}
	<p>
		{% if field.errors %}
		<ul class="errorlist">
			{% for error in field.errors %}
			<li>{{ error }}</li>
			{% endfor %}
		</ul>
		{% endif %}
	 	{{ field.label_tag }} {{ field }}
	</p>
	{% endfor %}
	<input type="submit" value="Register" />
</form>
```

## Registration logic

***views.py***

```python
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('blog')
        else:
            return render(request, 'users/register.html', {'form': form})
```

## Registration Form Link
```html
{%if request.user.is_authenticated %}

	<a href="{% url 'register' %}">Register</a>
{%endif%}

https://i.postimg.cc/gJkvTTXm/register1.png

