from .views import RegisterAPI, LoginAPI, MainUser 
from django.urls import path#, include

from knox import views as knox_views


urlpatterns = [
    #path('api/auth/', include('knox.urls')),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/auth/user/', MainUser.as_view()),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    ]

  