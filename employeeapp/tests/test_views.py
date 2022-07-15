'''Test cases for Employee Views'''
from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Employee
from random import randint

class EmployeeViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.employee = {
            "name" : "some name",
            "address" : "some where",
            "employee_number" : randint(2,200),
            "salary" : 20215,
            "date_of_birth" : "2022-02-20"
        }
        return self.employee
    def test_employee_view_get(self):
        self.url = reverse("employee")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    def test_employee_view_create(self):
        self.url = reverse("employee")
        response = self.client.post(self.url, self.employee)
        self.assertEqual(response.status_code, 201)

class EmployeeDetailTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.employee = {
            "name" : "some name",
            "address" : "some where",
            "employee_number" : randint(2,200),
            "salary" : 20215,
            "date_of_birth" : "2022-02-20"
        }   
        return self.employee
    def test_employee_view_get(self):
        self.url = reverse("employeedetail", args=[2])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_employee_view_put(self):
        self.employee_created = Employee.objects.create(
            name = "some name",
            address = "some where",
            employee_number = randint(2,200),
            salary = 20215,
            date_of_birth = "2022-02-20"
        )
        self.url = reverse("employeedetail", args=[self.employee_created.id])
        response = self.client.delete(self.url, self.employee)
        print(response.json())
        self.assertEqual(response.status_code, 200)