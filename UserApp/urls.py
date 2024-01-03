from django.urls import path
from .views import signup, login_view, dashboard, profile, logout_view

urlpatterns = [
    path('', signup, name='signup'),  # Redirect to the signup page
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
]
