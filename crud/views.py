# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string, get_template
from django.template import loader
from crud.forms import StudentForm
from crud.models import Student
# Create your views here.
def form(request):
    form_class = StudentForm()
    return render(request, 'crud/form.html', {"form":form_class})

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            stu_form=form.save(commit=False)
            stu_form.name = request.POST['name']
            stu_form.city = request.POST['city']
            stu_form.number = request.POST['number']
            # if request.POST['s_id']:
            #     obj = Name.objects.get(s_id=request.POST['s_id'])
            #     obj.name = request.POST['name']
            #     obj.city = request.POST['city']
            #     obj.number = request.POST['number']
            #     obj.save()
            stu_form.save()
    student_data = Student.objects.all()
    context = {
        "table_data": student_data,
    }
    table_html = render_to_string('crud/table.html', context)
    return HttpResponse(table_html)

@csrf_exempt
def edit(request):
    if request.method == 'POST':
        id= request.POST.get("s_id","")
        student, created = Student.objects.get_or_create(s_id=id)
        student.name = request.POST.get("name","")
        student.city = request.POST.get("city","")
        student.number = request.POST.get("number","")
        student.save()

        student_data = Student.objects.all()
        context = {
            "table_data": student_data,
        }
        table_html = render_to_string('crud/table.html', context)
        return HttpResponse(table_html)

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        id= request.POST.get("id","")
        student = Student.objects.filter(s_id=id).delete()
        student_data = Student.objects.all()
        context = {
            "table_data": student_data,
        }
        table_html = render_to_string('crud/table.html', context)
        return HttpResponse(table_html)
