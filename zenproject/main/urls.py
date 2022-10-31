from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home , name='home'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('edit/<int:id>', views.edit ,name='edit'),  
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'), 
] 