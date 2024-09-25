from django.db import models

class Task(models.Model):
    content = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    tags = models.ManyToManyField(to="Tag", related_name="tasks")

    class Meta:
        ordering = ["status", "date"]

    def __str__(self):
        return f"{self.content} (Done: {self.status})"


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name
