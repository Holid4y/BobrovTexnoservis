from django.shortcuts import render
from .models import record, staff

def index(request):
    return render(request, 'main/index.html')

def info(request):
    return render(request, 'main/info.html')

def contact(request):
    staffs = staff.objects.all()
    return render(request, 'main/contact.html', {'staff': staffs})

def about(request):
    return render(request, 'main/about.html')

def records(request):
    rec = record.objects.order_by('-date')[:20]
    return render(request, 'main/records.html', {'record': rec})