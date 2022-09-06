from django.urls import path
from .views import UserLoginView, UserProfileView, UserRegistrationView

urlpatterns = [
    path('profile/',UserProfileView.as_view(), name = "profile"),
    path('register/',UserRegistrationView.as_view(), name = "registration"),
    path('login/',UserLoginView.as_view(), name = 'login')
]