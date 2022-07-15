'''Employee  urls'''
from django.urls import path
from .views import EmployeeView, EmployeeDetailView

urlpatterns = [
    path("", EmployeeView.as_view(), name='employee'),
    path("<int:id>", EmployeeDetailView.as_view(), name='employeedetail'),
]