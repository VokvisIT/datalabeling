from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField

class MyModelFirst(models.Model):
    Data = models.DateField()
    Time = models.TimeField()
    Resource_Name = models.CharField(max_length=200)
    Header = models.CharField(max_length=200, null=True, blank=True)
    Text = models.TextField(null=True, blank=True)
    Comments_Count = models.IntegerField(null=True, blank=True)
    Views = models.IntegerField(null=True, blank=True)
    Rating = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Count_Positive_Reactions = models.IntegerField(null=True, blank=True)
    Count_Negative_Reactions = models.IntegerField(null=True, blank=True)
    Reposts = models.IntegerField(null=True, blank=True)
    Comment_Text = models.TextField(null=True, blank=True)
    Type = models.CharField(max_length=100)
    Garbage = models.BooleanField(null=True)
    Healthcare = models.BooleanField(null=True)
    Housing_and_Public_Utilities = models.BooleanField(null=True)
    Education = models.BooleanField(null=True)
    Infrastructure = models.BooleanField(null=True)
    Culture = models.BooleanField(null=True)
    Environmental_Conditions = models.BooleanField(null=True)
    Social_Security = models.BooleanField(null=True)
    Politics = models.BooleanField(null=True)
    Safety = models.BooleanField(null=True)
    Availability_of_Goods_and_Services = models.BooleanField(null=True)
    Official_Statements = models.BooleanField(null=True)
    Tourism = models.BooleanField(null=True)
    Facts = models.BooleanField(null=True)
    Positive = models.BooleanField(null=True)
    Negative = models.BooleanField(null=True)
    Neutral = models.BooleanField(null=True)
    def __str__(self):
        return f"ID: {self.id}. Текст с {self.Resource_Name}, тип: {self.Type}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    group_number = models.CharField(max_length=6, blank=True, null=True)
    count_task = models.IntegerField(blank=True, null=True, default=0)
    def __str__(self):
        return self.user.username

    @staticmethod
    def register(username,first_name, last_name, email, password, group_number):
        user = User.objects.create_user(
            username=username,
            first_name = first_name,
            last_name = last_name,
            email=email,
            password=password,
        )
        profile = Profile(user=user, group_number=group_number, count_task=0)
        profile.save()
        return profile