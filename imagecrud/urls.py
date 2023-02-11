from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('add/', views.add_image, name='add_image'),
    path('update/<int:pk>/', views.update_image, name='update_image'),
    path('delete/<int:pk>/', views.delete_image, name='delete_image'),
]