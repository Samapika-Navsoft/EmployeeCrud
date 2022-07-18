'''serializer class defined for Employee Model'''
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    '''Employee Serializer class'''
    employee_date_of_birth = serializers.SerializerMethodField("get_birth_date", read_only=True)
    class Meta:
        '''meta class for employee serializer'''
        model = Employee
        fields = ["id","name", "address", "employee_number", "salary", "employee_date_of_birth", "date_of_birth","created_at", "updated_at"]
        extra_kwargs = {
            "id":{
                "read_only": True
            },
            "created_at":{
                "read_only": True
            },
            "updated_at":{
                "read_only": True
            },
            "date_of_birth":{
                "write_only": True
            }
        }
    def get_birth_date(self, obj):
        if obj.date_of_birth:
            return obj.date_of_birth.strftime("%Y-%m-%d")



        
        

        
