from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
        return f"{self.name} - {self.subject}"

