from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerialzier,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins, generics,viewsets


# GET POST

@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerialzier(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerialzier(data=request.data)
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
        serializer = StudentSerialzier(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerialzier(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class Employees(APIView):
#     def get (self,request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#       # POST → Create a new employee
#     def post(self, request):
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class EmployeeDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
    
#     # GET → Retrieve a single employee
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # PUT → Update an existing employee
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # DELETE → Remove an employee
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # Mixins
# class Employees(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     # GET → List all employees
#     def get(self, request):
#         return self.list(request)
    
#     # POST -> create employees
#     def post(self,request):
#         return self.create(request)
 
# #Mixins    
# class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     # get using primary key
    
#     def get(self,request, pk):
#         return self.retrieve(request,pk)
    
#     # To update data using primary key
#     def put(self,request, pk):
#         return self.update(request,pk)
    
#     # delete object based on primary key
    
#     def delete(self,request, pk):
#         return self.destroy(request,pk)

# #Generics
# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# # Primary key based operations 
# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'

# ViewSets
# Get list of objects
class EmployeeViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset,many=True)
        return Response(serializer.data)
    
# create data
    def create(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)   


# Retrieve , Update and Delete object using Primary key using ViewSet

    def retrieve(self,request, pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        serializer  = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)   
    
    def update(self,request,pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(employee,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        