from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.http import HttpResponse



def index(request):
    images = Image.objects.all()
    return render(request, 'imagecrud/index.html', {'images': images})

def add_image(request):
      if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
      else:
          form = ImageForm()
      return render(request, 'imagecrud/add_image.html', {'form': form})




def update_image(request, pk):
    image = Image.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageForm(instance=image)
    return render(request, 'imagecrud/update_image.html', {'form': form})

def delete_image(request, pk):
    Image.objects.filter(pk=pk).delete()
    return redirect('index')
