from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employee, BlogPosts
# Create your views here.

def index(request):
    myEmployees = Employee.objects.all().values()
    template = loader.get_template('employee/index.html')
    context = {
        'myEmployees' : myEmployees
    }
    # print(context)
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('employee/createPage.html')
    return HttpResponse(template.render({}, request))

def createData(request):
    name = request.POST['name']
    title = request.POST['title']
    newEmployee = Employee(name=name, title=title)
    newEmployee.save()
    return HttpResponseRedirect(reverse('employee'))

def delete(request, id):
    deleteEmployee = Employee.objects.get(id=id)
    deleteEmployee.delete()
    return HttpResponseRedirect(reverse('employee'))

def update(request, id):
    updateEmployee = Employee.objects.get(id=id)
    template = loader.get_template('employee/updatePage.html')
    context = {
        'Employee': updateEmployee
    }
    return HttpResponse(template.render(context, request))

def updateData(request, id):
    name = request.POST['name']
    title = request.POST['title']
    updateEmployee = Employee.objects.get(id=id)
    updateEmployee.name = name
    updateEmployee.title = title
    updateEmployee.save()
    return HttpResponseRedirect(reverse('employee'))

def blog(request):
    posts = BlogPosts.objects.all()
    featuredPost = BlogPosts.objects.filter(featured=True)
    template = loader.get_template('employee/blog.html')
    context = {
        'posts': posts,
        'featuredPost': featuredPost
    }
    return HttpResponse(template.render(context, request))

def detailsPage(request, id):
    detailsPost = BlogPosts.objects.get(id=id)
    template = loader.get_template('employee/detailsPage.html')
    context = {
        'posts': detailsPost
    }
    return HttpResponse(template.render(context, request))