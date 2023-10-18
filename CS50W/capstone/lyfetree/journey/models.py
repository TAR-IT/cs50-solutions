from django.db import models
from django.contrib.auth.models import User  # If using Django's built-in User model


class Tag(models.Model): # Model for user-specific Lyfetree tags
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Milestone(models.Model): # Model for user-specific milestones
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link achievements to a user
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title