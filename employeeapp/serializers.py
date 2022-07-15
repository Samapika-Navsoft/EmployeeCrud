'''serializer class defined for Employee Model'''
from requests import request
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    '''Employee Serializer class'''
    date_of_birth = serializers.SerializerMethodField("get_birth_date", read_only=True)
    class Meta:
        '''meta class for employee serializer'''
        model = Employee
        fields = ["name", "address", "employee_number", "salary", "date_of_birth", "date_of_birth","created_at", "updated_at", "profile_picture"]
        extra_kwargs = {
            "created_at":{
                "read_only": True
            },
            "updated_at":{
                "read_only": True
            },
            "date_of_birth":{
                "write_only": True
            },
            "profile_picture":{
                "required": False
            },
        }
    def get_birth_date(self, obj):
        if obj.date_of_birth:
            return obj.date_of_birth.strftime("%Y-%m-%d")

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        

        
