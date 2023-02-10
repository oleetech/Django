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
