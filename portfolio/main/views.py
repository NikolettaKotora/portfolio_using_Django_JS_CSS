from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Project, Tag
from .forms import ContactForm

# Create your views here.
def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})

def project(request, id):
    project = get_object_or_404(Project, pk = id)
    return render(request, "project.html", {"project": project})

def success(request):
    if contact(request):
        return HttpResponse('Success!')
    else:
        return render(request, "success.html")
    

