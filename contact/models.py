from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"Contact Message {self.id} from {self.email}"