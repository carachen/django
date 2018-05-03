from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  render,render_to_response
# Create your views here.

def index(request):
	return HttpResponse ("Hello Django!")

def showStudents(request):  
    list = [{id: 1, 'name': 'Jack'}, {id: 2, 'name': 'Rose'}]  
    return render_to_response('student.html',{'students': list}) 
