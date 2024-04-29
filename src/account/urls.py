from django.urls import path
from django.views.generic import TemplateView
from .views import signup_login_view
urlpatterns = [
    path("signup_login/",signup_login_view , name='signup-login-view'),
    path("profil/", TemplateView.as_view(template_name = 'account/profil_user.html'), name='user_profil_view'),
]