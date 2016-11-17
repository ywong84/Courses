from django.shortcuts import render, redirect
from .models import course
# Create your views here.
def index(request):
    courses = course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'course/index.html', context)

def process(request):

    course.objects.create(course_name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def remove(request,id):
    context= {
        'course': course.objects.get(id=id)
    }
    return render(request, 'course/delete.html', context)

def delete(request, id):
    remove=course.objects.get(id=id)
    remove.delete()
    return redirect('/')
