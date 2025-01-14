# accounts/urls.py
from django.urls import path
from . import views




urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('add_blog/', views.add_blog, name='add_blog'),
    
    
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)