from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    message = models.CharField(max_length=500)
    is_responded = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact Message {self.id} from {self.email}"