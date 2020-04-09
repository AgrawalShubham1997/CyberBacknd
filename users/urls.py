from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.UserRegistration.as_view()),
    # path('login/', views.PostLogin.as_view())
]
