from django.urls import path
from .views import *


urlpatterns = [
    path('', login_check, name = 'login_check'),
    path('register/', register_view, name = 'register_view'),
    path('home/', home_view, name = 'home_view')

]
