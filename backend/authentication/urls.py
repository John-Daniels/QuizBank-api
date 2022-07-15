from django.urls import path

from .views import EmailVerificationView, LoginView, RegisterView

app_name = "authentication"
urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('email-verify', EmailVerificationView.as_view(), name="email-verify"),
]
