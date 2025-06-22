from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('internships/', views.internships, name='internships'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('extracurricular/', views.extracurricular, name='extracurricular'),
    path('contact/', views.contact, name='contact'),
]