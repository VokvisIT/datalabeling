from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .models import MyModelFirst, Profile

@admin.register(MyModelFirst)
class MyModelFirstAdmin(admin.ModelAdmin):
    list_display = 'id', 'Data', 'Time', 'Resource_Name', 'head_short', 'text_short', 'Garbage', 'Healthcare', 'Housing_and_Public_Utilities', 'Education', 'Infrastructure', 'Culture', 'Environmental_Conditions', 'Social_Security', 'Politics', 'Safety', 'Availability_of_Goods_and_Services', 'Official_Statements', 'Tourism', 'Facts', 'Positive', 'Negative', 'Neutral'
    ordering = '-Garbage',
    list_per_page = 15
    
    def text_short(self, obj: MyModelFirst):
        if len(obj.Text) < 10:
            return obj.Text
        return obj.Text[:10] + "..."
    
    def head_short(self, obj: MyModelFirst):
        try:
            if len(obj.Header) < 10:
                return obj.Header
            return obj.Header[:10] + "..."
        except:
            pass
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = 'id','user', 'count_task',
    ordering = 'count_task',
    list_per_page = 20
    def get_queryset(self, request: HttpRequest):
        return Profile.objects.select_related("user")