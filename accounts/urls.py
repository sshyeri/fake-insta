from django.urls import path
from .import views

app_name='accounts'

urlpatterns=[
    path('profile/update/', views.profile_update, name='profile_update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.password, name='password'),
    path('update/', views.update, name='update'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    ]
