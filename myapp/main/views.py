from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Record
from .forms import RecordForm

def index(request):
    records = Record.objects.all()
    return render(request, 'index.html', {'records': records})

def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecordForm()
    return render(request, 'add_record.html', {'form': form})

def edit_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecordForm(instance=record)
    return render(request, 'edit_record.html', {'form': form})

def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    record.delete()
    return redirect('index')
