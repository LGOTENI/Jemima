from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('ajouter/', views.post_new, name='add'), 
    path('modifier/<int:id>', views.update, name='update'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
    
]
