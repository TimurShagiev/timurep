from django.db import models
from django.contrib.auth.models import User


class Problem(models.Model):
    PRIORITIES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    STATUS_CHOICES = (
        ('new', 'New'),
        ('In progress', 'In progress'),
        ('resolved', 'Resolved'),
        ('confirmed', 'Confirmed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITIES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    actions = models.TextField(blank=True)

    assigned_user = models.ForeignKey(User, related_name='assigned_problems', null=True, blank=True, on_delete=models.SET_NULL)
    resolved_user = models.ForeignKey(User, related_name='resolved_problems', null=True, blank=True, on_delete=models.SET_NULL)

    # objects = models.Manager()
