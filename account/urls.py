
from django.urls import path,include
from .import views
urlpatterns = [

    path('Signup/',views.signup),
    path('Login/',views.log),
    path('Logout/',views.user_logout)
    
]
