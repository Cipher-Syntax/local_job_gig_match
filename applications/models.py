from django.db import models
from accounts.models import User
from jobs.models  import Gig

# Create your models here.
class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='pending')
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"{self.job_seeker.username} applied for {self.gig.title}"