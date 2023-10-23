from django.db import models
from django.contrib.auth.models import User, AbstractUser

# User model
class User(AbstractUser):
    pass

# Diary Entry model
class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    title = models.CharField(max_length=100)
    content = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favourized = models.ManyToManyField(User, related_name='favourized_entries', blank=True)

    def __str__(self):
        return self.title

# Comment model (additional feature)
class EntryComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    entry = models.ForeignKey(DiaryEntry, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commented on {self.created_at}"