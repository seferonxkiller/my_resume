from django.db import models
from post.models import Category


# Create your models here.


class Partner(models.Model):
    image = models.ImageField(upload_to='icon')

    def __str__(self):
        return self.image.name


class About(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='author')
    birthday = models.DateField()
    bio = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    projects = models.IntegerField()

    def __str__(self):
        return self.name


class Projects(models.Model):
    image = models.ImageField(upload_to='projects')
    category = models.ManyToManyField(Category, blank=True)
    link = models.URLField(null=True, blank=True)
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.profession


class Resume(models.Model):
    type = models.CharField(max_length=255)
    is_skill = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class AdditionalInfo(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    # experience
    profession = models.CharField(max_length=255, blank=True, null=True)
    start_finish = models.CharField(max_length=255, null=True, blank=True)
    academy = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    # is skill
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Skill name')
    percent = models.IntegerField(null=True, blank=True)
    is_main = models.BooleanField(default=False)

    @property
    def last_week(self):
        lw = self.percent / 4
        return round(lw)

    @property
    def last_month(self):
        lm = self.percent / 12
        return round(lm)
