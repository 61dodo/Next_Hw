"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.home, name='home'),
   path('new/', views.new, name='new'),
   path('detail/<int:post_pk>', views.detail, name='detail'),
   path('edit/<int:post_pk>', views.edit, name='edit'),
   path('delete/<int:post_pk>', views.delete, name='delete'),
   path('delete-comment/<int:post_pk>/<int:comment_pk>', views.delete_comment, name='delete_comment'),
   path("registration/signup/", views.signup, name="signup"),
   path("registration/login/", views.login, name="login"),
   path("registration/logout/", views.logout, name="logout"),
   path("like", views.like, name="like"),
   path('add-comment/<int:post_pk>/', views.add_comment, name='add_comment'),
   path('delete-comment/<int:post_pk>/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
]

