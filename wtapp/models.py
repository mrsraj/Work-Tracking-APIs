from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 

class CustomUser (AbstractUser):
    # Add any additional fields you want
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    column = models.CharField(max_length=20)  # e.g., column1, column2, column3
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    

class Board(models.Model):
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)


# class BoardMember(models.Model):
#     creation_timestamp = models.DateTimeField(auto_now_add=True)
#     created_by = models.CharField(max_length=200)
#     modification_timestamp = models.DateTimeField(auto_now=True)
#     modified_by = models.CharField(max_length=200)
#     board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='members')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
#     board_name = models.CharField(max_length=200)
#     member_name = models.CharField(max_length=200)

#     def __str__(self):
#         return f"{self.member_name} in {self.board.name}"