from django.urls import path
from .import views

app_name='accounts'

urlpatterns=[
    path('delete/', views.delete, name='delete'),
    path('password/', views.password, name='password'),
    path('update/', views.update_profile, name='update_profile'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    ]
