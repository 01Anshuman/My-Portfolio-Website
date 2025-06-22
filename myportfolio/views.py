from django.shortcuts import render
from .models import Education, Internship, Project, TechnicalSkill, Extracurricular, Contact
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, 'myportfolio/home.html')

def education(request):
    educations = Education.objects.all()
    return render(request, 'myportfolio/education.html', {'educations': educations})

def internships(request):
    internships = Internship.objects.all()
    return render(request, 'myportfolio/internships.html', {'internships': internships})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'myportfolio/projects.html', {'projects': projects})

def skills(request):
    skills = TechnicalSkill.objects.all()
    return render(request, 'myportfolio/skills.html', {'skills': skills})

def extracurricular(request):
    extracurriculars = Extracurricular.objects.all()
    return render(request, 'myportfolio/extracurricular.html', {'extracurriculars': extracurriculars})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return render(request, 'myportfolio/contact.html', {'form': ContactForm()})
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'myportfolio/contact.html', {'form': form})