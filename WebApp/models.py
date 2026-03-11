from django.db import models

# Create your models here.

class UserDb(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Confirm_password = models.CharField(max_length=100)

class ContactDb(models.Model):
    Full_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=150)
    Mobile = models.CharField(max_length=20)
    Description = models.TextField()
    

class IssueDb(models.Model):
    STATUS_UNSOLVED = "unsolved"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_SOLVED = "solved"
    STATUS_CHOICES = [
        (STATUS_UNSOLVED, "Unsolved"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_SOLVED, "Solved"),
    ]

    Category = models.CharField(max_length=100)
    Image = models.ImageField(upload_to="issues", null=True, blank=True)
    Description = models.TextField()
    Contact_Number = models.CharField(max_length=20)
    Latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    Longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    Location = models.CharField(max_length=255)
    Created_Date = models.DateTimeField(auto_now_add=True)
    Username = models.CharField(max_length=100,null=True,blank=True)
    Status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=STATUS_UNSOLVED,)

class CommentDb(models.Model):
    Comment = models.TextField()
    Username = models.CharField(max_length=100,null=True,blank=True)
    Issue = models.ForeignKey(IssueDb, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
