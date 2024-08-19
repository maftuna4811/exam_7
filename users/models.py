from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=200)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment_title}'

    class Meta:
        ordering = ['id', 'user']
        indexes = [
            models.Index(fields=['id', 'user'])
        ]


class Problems(models.Model):
    firstname = models.CharField(max_length=30)
    email = models.EmailField()
    problem_name = models.CharField(max_length=30)
    problem_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.problem_name}'

    class Meta:
        ordering = ['id', 'created_at']
        indexes = [
            models.Index(fields=['id', 'firstname'])
        ]


class Advisers(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='users/advisers/')
    phone = models.CharField(max_length=30)
    profession = models.CharField(max_length=60, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        ordering = ['id', 'firstname', 'lastname']
        indexes = [
            models.Index(fields=['id', 'firstname', 'lastname', 'username'])
        ]

