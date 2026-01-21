from django.db import models
from users.models import User

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Permission(models.Model):
    ACTIONS = [
        ('READ', 'Read'),
        ('WRITE', 'Write'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTIONS)
