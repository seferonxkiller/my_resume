from django.db import models

# Create your models here.


class GitInTouch(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    icon = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.profession
