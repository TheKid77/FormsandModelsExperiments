from django.db import models
from .employee import Employee

class AnnualReview(models.Model):
    employee = models.ForeignKey (
        Employee,
        on_delete=models.CASCADE,
        related_name = 'reviews'
    )
    year = models.IntegerField()
    review = models.TextField()
 