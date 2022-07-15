import imp
from django.test import TestCase
from django.urls import reverse, resolve
from ..views import EmployeeView, EmployeeDetailView

class EmployeeUrlTest(TestCase):
    def test_employee_get_create(self):
        self.url = reverse("employee")
        self.assertEqual(resolve(self.url).func.view_class, EmployeeView)
    def test_employee_get_update_delete(self):
        self.url = reverse("employeedetail", args=[2])
        self.assertEqual(resolve(self.url).func.view_class, EmployeeDetailView)
