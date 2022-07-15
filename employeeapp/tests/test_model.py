'''Employee Model Test'''
from django.test import TestCase
from ..models import Employee
from random import randint

class EmployeeModelTest(TestCase):
    def setUp(self) -> None:
        self.employee = Employee.objects.create(
            name = "some name",
            address = "some where",
            employee_number = randint(2,200),
            salary = 20215,
            date_of_birth = "2022-02-20"
        )
        return self.employee
    def test_create_employee(self):
        self.assertTrue(isinstance(self.employee, Employee))