from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

# Add related names for the groups and user_permissions fields to avoid clashes
User._meta.get_field('groups').remote_field.related_name = 'custom_user_set'
User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_set'
