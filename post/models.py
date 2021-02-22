from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=255, default='0000000')
    text = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
