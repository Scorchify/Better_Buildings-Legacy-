from django.db import models
from django.utils import timezone

class Report(models.Model):
    CATEGORIES = [
        ('', 'Select'),  # Default option
        ('Bathrooms', 'Bathrooms'),
        ('Building', 'Building'),
        ('Other', 'Other')
    ]
    
    q1 = models.TextField(
        blank=False,  # Ensures the field is required
        default='',
    )
    q2 = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        default='',
    )
    submitted_at = models.DateTimeField(
        auto_now_add=True,  # Automatically set the field to the current timestamp when the object is created
        editable=False,     # Prevent manual editing of this field
    )
    upvotes = models.IntegerField(
        default=0,  
    )

    def __str__(self):
        return f"Report {self.id} - {self.q2}"
    
    def upvote(self): #upvotes for later
        self.upvotes += 1
        self.save()

