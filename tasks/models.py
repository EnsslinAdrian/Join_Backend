from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30, null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)

class Task(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="tasks")
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    date = models.CharField(max_length=30)
    prio = models.CharField(max_length=30)
    prioImg = models.CharField(max_length=80)
    taskCategory = models.CharField(max_length=30)
    subtasks = models.JSONField(default=list)
    taskContacts = models.JSONField(default=list)
    


