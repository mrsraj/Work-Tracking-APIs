from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 

class CustomUser (AbstractUser):
    # Add any additional fields you want
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
    
class ToDoTask(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    

class User(models.Model):
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    modification_timestamp = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

class Board(models.Model):
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    modification_timestamp = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    # logo = models.ImageField(upload_to='board_logos/', blank=True, null=True)

    def __str__(self):
        return self.name


class CardCategory(models.Model):
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    modification_timestamp = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='categories')
    sort_order = models.PositiveIntegerField()

   
class Card(models.Model):
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    modification_timestamp = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    category = models.ForeignKey(CardCategory, on_delete=models.SET_NULL, null=True, related_name='cards')
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self.subject


class BoardMember(models.Model):
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    modification_timestamp = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=200)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    board_name = models.CharField(max_length=200)
    member_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.member_name} in {self.board.name}"