from django.db import models
from accounts.models import User
# Create your models here.
class Gig(models.Model):
    STATUS_CHOICES = [
        ('o', 'Open'),
        ('f', 'Filled'),
        ('c', 'Closed')
    ]
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False, null=False)
    location = models.CharField(max_length=255)
    pay = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    