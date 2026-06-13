#from django.shortcuts import render
#from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerialier
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# GET POST

@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerialier(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# GET, POST, DELETE

@api_view(['GET','PUT','DELETE'])
def StudentDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerialier(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerialier(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)