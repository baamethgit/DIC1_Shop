from django.urls import path
from django.views.generic import TemplateView
from .views import signup_login_view,signup_view_2,updateUser,logout_user
urlpatterns = [
    path("signup_login/",signup_login_view , name='signup-login-view'),
    path('signup2/',signup_view_2,name='signup_step2'),
    path("profil/", TemplateView.as_view(template_name = 'account/profil_user.html'), name='user_profil_view'),
    path('edit/', updateUser, name='edit-user-view'),
    path('logout/',logout_user, name = 'logout'),
    path('<str:blabla>/',TemplateView.as_view(template_name= '404.html'))
]