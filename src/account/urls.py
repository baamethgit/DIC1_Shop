from django.urls import path
from django.views.generic import TemplateView
from .views import login_user,signup_user
urlpatterns = [
    # path("signin/", TemplateView.as_view(template_name = 'account/signin.html'), name='signup_view'),
    path("signin/",signup_user , name='signup_view'),
    path("profil/", TemplateView.as_view(template_name = 'account/profil_user.html'), name='user_profil_view'),
]
