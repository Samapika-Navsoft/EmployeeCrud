'''Employees views'''
import re
from urllib import response
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from uritemplate import partial
from .serializers import EmployeeSerializer, Employee, EmployeeUpdateSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from django.shortcuts import  get_object_or_404

employee_get_update_response = {
    "200": EmployeeSerializer,
    "400": openapi.Response("Data Not Found")
}

employee_create_response = {
    "201": openapi.Response("Created"),
    "400": openapi.Response("Data Not Found")
}

class EmployeeView(GenericAPIView):
    parser_classes =[MultiPartParser]
    serializer_class = EmployeeSerializer
    @swagger_auto_schema(tags=["Employee"], operation_description="Emloyee List", operation_summary="Employee List", responses=employee_get_update_response)
    def get(self, request):
        http_status = None
        response = {}
        employees = Employee.objects.all()
        serializer = self.serializer_class(employees, many=True)
        response["data"] = serializer.data
        http_status = status.HTTP_200_OK
        return Response(response,http_status)
    @swagger_auto_schema(tags=["Employee"], operation_description="Emloyee Create", operation_summary="Employee Create", responses=employee_create_response)
    def post(self, request):
        http_status = None
        response = {}
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response["message"] = "Employee created successfully"
        response["data"] = serializer.data
        http_status = status.HTTP_201_CREATED
        return Response(response,http_status)

class EmployeeDetailView(GenericAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = EmployeeSerializer
    def get_employee(self, id):
        employee = Employee.objects.filter(id=id).first()
        return employee
    @swagger_auto_schema(tags=["Employee"], operation_description="Emloyee Get", operation_summary="Employee Get", responses=employee_get_update_response)
    def get(self, request, id):
        response = {}
        http_status = None
        employee = self.get_employee(id)
        employee_serializer = self.serializer_class(employee).data
        response["data"] = employee_serializer
        http_status = status.HTTP_200_OK
        return Response(response, http_status)
    @swagger_auto_schema(tags=["Employee"], operation_description="Emloyee Update", operation_summary="Employee Update", responses=employee_get_update_response)
    def put(self, request, id):
        response = {}
        http_status = None
        employee = self.get_employee(id)
        serialized_data = self.serializer_class(employee, data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response["message"] = "Data updated"
        response["data"] = serialized_data.data
        http_status = status.HTTP_200_OK
        return Response(response, http_status)
    @swagger_auto_schema(tags=["Employee"], operation_description="Emloyee partial Update", operation_summary="Employee partial Update", responses=employee_get_update_response)
    def patch(self, request, id):
        response = {}
        http_status = None
        employee = self.get_employee(id)
        serialized_data = EmployeeUpdateSerializer(employee, data=request.data, partial=True)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response["message"] = "Data updated"
        response["data"] = serialized_data.data
        http_status = status.HTTP_200_OK
        return Response(response, http_status)
    @swagger_auto_schema(tags=["Employee"], operation_description="Emloyee Delete", operation_summary="Employee Delete")
    def delete(self, request, id):
        response = {}
        http_status = None
        employee = self.get_employee(id)
        employee.delete()
        response["message"] = "data deleted"
        http_status = status.HTTP_200_OK
        return Response(response, http_status)



        






