from django.urls import path
from .views import (
    IndexView,
    UserLoginView, UserHomeView, UserLogoutView,
    ContactFormView, PrivacyPolicyView
)

app_name = 'account'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', UserLoginView.as_view(), name='login'),
    path('home', UserHomeView.as_view(), name='home'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('contact', ContactFormView.as_view(), name='contact'),
    path('privacy-policy', PrivacyPolicyView.as_view(), name='privacy_policy')
]
