from django.shortcuts import render
from django.http import JsonResponse

def studentsView(request):
    students = [
        {
            'id':1,
            'name':'Ratan',
            'class':'Computer Science'
        }
    ]
    return JsonResponse({'students': students})