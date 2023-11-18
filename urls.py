from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import user_profile

urlpatterns = [
    path("admin/", admin.site.urls),
    path('profile/', views.user_profile, name='user_profile'),
]