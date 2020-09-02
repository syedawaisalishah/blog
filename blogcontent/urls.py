
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home),
    path('Blogs/<int:id>/<str:slug>',views.blogs),
  
    path('Search/',views.search),
]
