from django.urls import path
from .views import login_view, register_view, qest, logout_view
app_name = "labeling"
urlpatterns = [
  path('', qest, name='qest'),
  path('login/', login_view, name='login'),
  path('register/', register_view, name='register'),
  path('logout/', logout_view, name='logout'),
]