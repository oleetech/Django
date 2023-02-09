
# Student Crud 

A Student Information Crud .
```bash
 ____       _                                      ____                      _ 
 |  _ \    (_)   __ _   _ __     __ _    ___      / ___|  _ __   _   _    __| |
 | | | |   | |  / _` | | '_ \   / _` |  / _ \    | |     | '__| | | | |  / _` |
 | |_| |   | | | (_| | | | | | | (_| | | (_) |   | |___  | |    | |_| | | (_| |
 |____/   _/ |  \__,_| |_| |_|  \__, |  \___/     \____| |_|     \__,_|  \__,_|
         |__/                   |___/                                          

                             ____   __   __
                            | __ )  \ \ / /
                            |  _ \   \ V / 
                            | |_) |   | |  
                            |____/    |_|  
                              
         ___    _                 _____                 _         
        / _ \  | |   ___    ___  |_   _|   ___    ___  | |__      
       | | | | | |  / _ \  / _ \   | |    / _ \  / __| | '_ \     
       | |_| | | | |  __/ |  __/   | |   |  __/ | (__  | | | |    
        \___/  |_|  \___|  \___|   |_|    \___|  \___| |_| |_|    


``` 
![Logo](https://i.postimg.cc/wTT53xhq/Student-Crud.png)

****create an app using the following command****
```bash
python manage.py startapp students
```
****Add App With Django Project****
```python

INSTALLED_APPS = [
    'students',
]
```
****create a model: In the models.py file of the students app, define a model for the students.****       
##  models.py 
```bash
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_of_birth = models.DateField()
```
****Create a form: In the forms.py file of the students app****

***forms.py***
```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth']
```

****Create views: In the views.py file of the students app****

***views.py***
```python
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')

```

****Create templates: Create templates for the student list, create, update and delete operations****

***templates/students/student_list.html***
```html

<h1>Student List</h1>

<table>
  <thead>
    <tr>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Email</th>
      <th>Date of Birth</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {% for student in students %}
    <tr>
      <td>{{ student.first_name }}</td>
      <td>{{ student.last_name }}</td>
      <td>{{ student.email }}</td>
      <td>{{ student.date_of_birth }}</td>
      <td>
        <a href="{% url 'student_update' student.id %}">Edit</a> |
        <a href="{% url 'student_delete' student.id %}" onclick="return confirm('Are you sure?');">Delete</a>
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<a href="{% url 'student_create' %}">Add Student</a>

```
***templates/students/student_form.html***

```html
<h1>{% if form.instance.id %}Edit{% else %}Add{% endif %} Student</h1>

<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>

<a href="{% url 'student_list' %}">Back to list</a>
```
****Create URL patterns: In the urls.py file of the students app****
***urls.py***
```python
from django.urls import path
from .views import student_list, student_create, student_update, student_delete

urlpatterns = [
    path('', student_list, name='student_list'),
    path('create/', student_create, name='student_create'),
    path('update/<int:id>/', student_update, name='student_update'),
    path('delete/<int:id>/', student_delete, name='student_delete'),
]

```
*****Link student app urls.py with project urls.py****

*****Run migrations*****
```bash
python manage.py makemigrations
python manage.py migrate
```
![Logo](https://i.postimg.cc/wTT53xhq/Student-Crud.png)
