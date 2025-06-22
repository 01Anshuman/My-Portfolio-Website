from django.db import models

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    cgpa_or_percentage = models.CharField(max_length=10)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Internship(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=100)
    technologies = models.CharField(max_length=100)
    github_link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

class TechnicalSkill(models.Model):
    category = models.CharField(max_length=50)
    skills = models.TextField()

    def __str__(self):
        return self.category

class Extracurricular(models.Model):
    title = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"