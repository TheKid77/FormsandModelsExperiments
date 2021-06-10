from enum import unique
from django.db import models
from .person import Person
from django.utils.translation import gettext_lazy as _
import datetime

class Employee (Person):
    class EmployeeType(models.TextChoices):
        FULLTIMEEMPLOYEE = 'FTE', _('Full Time Employee')
        PARTTIMEEMPLOYEE = 'PTE', _('Part Time Employee')
        PARTTIMECONTRACTOR = 'PTC', _('Part Time Contractor')
        FULLTIMECONTRACTOR = 'FTC', _('Full Time Contractor')

    employee_no = models.IntegerField(unique=True)
    date_joined = models.DateField()
    employee_type = models.CharField(
        max_length=25,
        choices=EmployeeType.choices,
        default=EmployeeType.FULLTIMEEMPLOYEE,
    )
  
