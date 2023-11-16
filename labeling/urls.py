from django.urls import path
from .views import login_view, register_view, qest
app_name = "labeling"
urlpatterns = [
  path('', login_view, name='login'),
  path('register/', register_view, name='register'),
  path('qest/', qest, name='qest'),
]