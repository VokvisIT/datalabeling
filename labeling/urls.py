from django.urls import path
from .views import qest
app_name = "labeling"
urlpatterns = [
  path("", qest, name="qest")
]