from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(default="No description provided.")
    completed = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.id} {self.name} {self.description} {str(self.completed)}"

