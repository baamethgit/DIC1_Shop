from django.urls import path
from django.views.generic import TemplateView
urlpatterns = [
    path("signin/", TemplateView.as_view(template_name = 'account/signin.html'), name='signup_view'),
]
