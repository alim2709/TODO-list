from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    content = models.TextField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name="tasks")

    class Meta:
        ordering = ["-is_completed", "-datetime"]

    def __str__(self) -> str:
        return self.name
