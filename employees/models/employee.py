from django.db import models
from .person import Person

class Employee (Person):

    employee_no = models.IntegerField(blank=True)
